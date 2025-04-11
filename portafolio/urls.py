from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("proyectos/", views.proyectos, name="proyectos"),
    path("contacto/", views.contacto, name="contacto"),
    path("proyecto_chatbot/", views.proyecto_chatbot, name="proyecto_chatbot"),
    path("proyecto_prob_partidos/", views.proyecto_prob_partidos, name="proyecto_prob_partidos"),
]