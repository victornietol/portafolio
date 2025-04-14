from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("proyectos/", views.proyectos, name="proyectos"),
    path("contacto/", views.contacto, name="contacto"),
    path("proyecto_chatbot/", views.proyecto_chatbot, name="proyecto_chatbot"),
    path("proyecto_prob_partidos/", views.proyecto_prob_partidos, name="proyecto_prob_partidos"),
    path("proyecto_recomendador_beb/", views.proyecto_recomendador_beb, name="proyecto_recomendador_beb"),
    path("proyecto_gestor_presupuestos/", views.proyecto_gestor_presupuestos, name="proyecto_gestor_presupuestos"),
    path("proyecto_guia_videojuego/", views.proyecto_guia_videojuego, name="proyecto_guia_videojuego"),
]