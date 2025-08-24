from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.contrib import messages
import csv, io

from .models import Persona
from .forms import PersonaForm
from oficinas.models import Oficina

class PersonaListView(ListView):
    model = Persona
    paginate_by = 10
    template_name = 'personas/listado.html'
    context_object_name = 'personas'

class PersonaDetailView(DetailView):
    model = Persona
    template_name = 'personas/detalle.html'
    context_object_name = 'persona'

class PersonaCreateView(LoginRequiredMixin, CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'personas/form.html'
    success_url = reverse_lazy('personas:listado')

class PersonaUpdateView(LoginRequiredMixin, UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'personas/form.html'
    success_url = reverse_lazy('personas:listado')

class PersonaDeleteView(LoginRequiredMixin, DeleteView):
    model = Persona
    template_name = 'personas/confirmar_eliminar.html'
    success_url = reverse_lazy('personas:listado')

def buscar(request):
    # Barra de búsqueda del navbar: busca por nombre o apellido. Lo básico y efectivo.
    q = request.GET.get('q', '').strip()
    personas = Persona.objects.all()
    if q:
        personas = personas.filter(nombre__icontains=q) | personas.filter(apellido__icontains=q)
    paginator = Paginator(personas, 10)
    page = request.GET.get('page')
    personas_page = paginator.get_page(page)
    return render(request, 'personas/listado.html', {'personas': personas_page, 'q': q})

@login_required
def carga_masiva_personas(request):
    # CSV con: apellido,nombre,edad,oficina_nombre_corto
    if request.method == 'POST' and request.FILES.get('archivo'):
        archivo = request.FILES['archivo']
        try:
            decoded = archivo.read().decode('utf-8')
            reader = csv.DictReader(io.StringIO(decoded), fieldnames=['apellido','nombre','edad','oficina_nc'])
            creadas, errores = 0, 0
            for row in reader:
                apellido = (row.get('apellido') or '').strip()
                nombre = (row.get('nombre') or '').strip()
                edad_str = (row.get('edad') or '').strip()
                oficina_nc = (row.get('oficina_nc') or '').strip()

                if not all([apellido, nombre, edad_str, oficina_nc]):
                    errores += 1
                    continue
                try:
                    edad = int(edad_str)
                except:
                    errores += 1
                    continue
                try:
                    oficina = Oficina.objects.get(nombre_corto=oficina_nc)
                except Oficina.DoesNotExist:
                    errores += 1
                    continue
                Persona.objects.create(apellido=apellido, nombre=nombre, edad=edad, oficina=oficina)
                creadas += 1
            messages.success(request, f'Personas creadas: {creadas}. Filas con error: {errores}.')
            return redirect('personas:listado')
        except Exception as e:
            messages.error(request, f'Algo explotó con el CSV: {e}')
    return render(request, 'carga_masiva.html', {'titulo':'Carga masiva de personas'})
