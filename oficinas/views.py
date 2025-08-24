from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.contrib import messages
import csv, io

from .models import Oficina
from .forms import OficinaForm
from personas.models import Persona

class OficinaListView(ListView):
    model = Oficina
    paginate_by = 10
    template_name = 'oficinas/listado.html'
    context_object_name = 'oficinas'

class OficinaDetailView(DetailView):
    model = Oficina
    template_name = 'oficinas/detalle.html'
    context_object_name = 'oficina'

class OficinaCreateView(LoginRequiredMixin, CreateView):
    model = Oficina
    form_class = OficinaForm
    template_name = 'oficinas/form.html'
    success_url = reverse_lazy('oficinas:listado')

class OficinaUpdateView(LoginRequiredMixin, UpdateView):
    model = Oficina
    form_class = OficinaForm
    template_name = 'oficinas/form.html'
    success_url = reverse_lazy('oficinas:listado')

class OficinaDeleteView(LoginRequiredMixin, DeleteView):
    model = Oficina
    template_name = 'oficinas/confirmar_eliminar.html'
    success_url = reverse_lazy('oficinas:listado')

def buscar(request):
    # Para oficinas no hay barra de búsqueda global, pero lo dejo por si pinta filtrar.
    q = request.GET.get('q', '').strip()
    oficinas = Oficina.objects.all()
    if q:
        oficinas = oficinas.filter(nombre__icontains=q) | oficinas.filter(nombre_corto__icontains=q)
    paginator = Paginator(oficinas, 10)
    page = request.GET.get('page')
    oficinas_page = paginator.get_page(page)
    return render(request, 'oficinas/listado.html', {'oficinas': oficinas_page, 'q': q})

@login_required
def carga_masiva_oficinas(request):
    # Subís un CSV de oficinas y listo. Formato: nombre,nombre_corto
    if request.method == 'POST' and request.FILES.get('archivo'):
        archivo = request.FILES['archivo']
        try:
            decoded = archivo.read().decode('utf-8')
            reader = csv.DictReader(io.StringIO(decoded), fieldnames=['nombre','nombre_corto'])
            creadas, existentes = 0, 0
            for row in reader:
                nombre = (row.get('nombre') or '').strip()
                nombre_corto = (row.get('nombre_corto') or '').strip()
                if not nombre or not nombre_corto:
                    continue
                obj, created = Oficina.objects.get_or_create(nombre_corto=nombre_corto, defaults={'nombre': nombre})
                if created:
                    creadas += 1
                else:
                    existentes += 1
            messages.success(request, f'Cargadas {creadas}. Ya existían {existentes}.')
            return redirect('oficinas:listado')
        except Exception as e:
            messages.error(request, f'Pifiaste el CSV? Error: {e}')
    return render(request, 'carga_masiva.html', {'titulo':'Carga masiva de oficinas'})
