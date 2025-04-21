from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html',{ 
        'pagina_actual':'index'
    })

def proyectos(request):
    return render(request, 'proyectos.html', {
        'pagina_actual':'proyectos'
    })

def contacto(request):
    return render(request, 'contacto.html', {
        'pagina_actual':'contacto'
    })

def proyecto_chatbot(request):
    return render(request, 'proyectos/chatbot.html', {
        'pagina_actual':'proyectos'
    })

def proyecto_prob_partidos(request):
    return render(request, 'proyectos/prob_partidos.html', {
        'pagina_actual':'proyectos'
    })

def proyecto_recomendador_beb(request):
    return render(request, 'proyectos/recomendador_beb.html', {
        'pagina_actual':'proyectos'
    })

def proyecto_gestor_presupuestos(request):
    return render(request, 'proyectos/gestor_presupuestos.html', {
        'pagina_actual':'proyectos'
    })

def proyecto_guia_videojuego(request):
    return render(request, 'proyectos/guia_videojuego.html', {
        'pagina_actual':'proyectos'
    })

def proyecto_bases_datos_sql(request):
    return render(request, 'proyectos/bases_datos_sql.html', {
        'pagina_actual':'proyectos'
    })

def proyecto_compilador_sencillo(request):
    return render(request, 'proyectos/compilador_sencillo.html', {
        'pagina_actual':'proyectos'
    })

def proyecto_videojuegos(request):
    return render(request, 'proyectos/videojuegos.html', {
        'pagina_actual':'proyectos'
    })

def proyecto_algoritmoGenetico_AFD(request):
    return render(request, 'proyectos/algoritmoGenetico_AFD.html', {
        'pagina_actual':'proyectos'
    })

def proyecto_practica_cifrado(request):
    return render(request, 'proyectos/practica_cifrado.html', {
        'pagina_actual':'proyectos'
    })