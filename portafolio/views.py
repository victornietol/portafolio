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