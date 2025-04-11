from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("proyectos/", views.proyectos, name="proyectos"),
    path("contacto/", views.contacto, name="contacto"),
    path("proyecto_chatbot/", views.proyecto_chatbot, name="proyecto_chatbot"),
]