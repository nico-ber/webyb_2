from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("inicio/", views.inicio, name="inicio"),
    path("servicios/", views.servicios, name="servicios"),
    path("sobre/", views.sobre, name="sobre"),
    path("contacto/", views.contacto, name="contacto"),
]

