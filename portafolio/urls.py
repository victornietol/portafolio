from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("proyectos/", views.proyectos, name="proyectos"),
    path("contacto/", views.contacto, name="contacto"),
    path("proyectos/proyecto_chatbot/", views.proyecto_chatbot, name="proyecto_chatbot"),
    path("proyectos/proyecto_prob_partidos/", views.proyecto_prob_partidos, name="proyecto_prob_partidos"),
    path("proyectos/proyecto_recomendador_beb/", views.proyecto_recomendador_beb, name="proyecto_recomendador_beb"),
    path("proyectos/proyecto_gestor_presupuestos/", views.proyecto_gestor_presupuestos, name="proyecto_gestor_presupuestos"),
    path("proyectos/proyecto_guia_videojuego/", views.proyecto_guia_videojuego, name="proyecto_guia_videojuego"),
    path("proyectos/proyecto_bases_datos_sql/", views.proyecto_bases_datos_sql, name="proyecto_bases_datos_sql"),
    path("proyectos/proyecto_compilador_sencillo/", views.proyecto_compilador_sencillo, name="proyecto_compilador_sencillo"),
    path("proyectos/proyecto_videojuegos/", views.proyecto_videojuegos, name="proyecto_videojuegos"),
    path("proyectos/proyecto_algoritmoGenetico_AFD/", views.proyecto_algoritmoGenetico_AFD, name="proyecto_algoritmoGenetico_AFD"),
    path("proyectos/proyecto_practica_cifrado/", views.proyecto_practica_cifrado, name="proyecto_practica_cifrado"),
]