from django.shortcuts import render
from django.http import HttpResponse
from .forms import EnviarMensaje
from django.core.mail import send_mail
from django.utils.translation import gettext as _
from .models import servicio


def index(response):
    return render(response, "main/base.html", {})

def inicio(request):
    servicios = servicio.objects.all()
    return render(request, "main/inicio.html", {'servicios': servicios})
    
def servicios(response):
    servicios = servicio.objects.all()
    return render(response, "main/servicios.html", {'servicios': servicios})

def sobre(response):
    return render(response, "main/sobre.html", {})

def contacto(request):
    if request.method == 'GET':
        form = EnviarMensaje()
    else:
        form = EnviarMensaje(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            desde_email = form.cleaned_data['desde_email']
            mensaje     = form.cleaned_data['mensaje']
            send_mail("Consulta", "Enviado por: "+desde_email+"\n\nNombre: "+nombre+ "\n\nMensaje: " +mensaje, desde_email, ['queve.franc@gmail.com'], fail_silently=False)
    return render(request, "main/contacto.html", {"form":form})
