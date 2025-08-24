from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistroForm

def registro(request):
    # Nada del otro mundo: si es POST valido el form y lo creo.
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Te registraste ok. Meté login y a jugar.')
            return redirect('accounts:login')
        else:
            messages.error(request, 'Fijate que hay errores.')
    else:
        form = RegistroForm()
    return render(request, 'accounts/registro.html', {'form': form})
