from django.shortcuts import render
from administrativo.models import Estudiante

def listado_nuevo(request):
    estudiantes = Estudiante.objects.all()
    informacion_template = {
        'estudiantes': estudiantes,
        'numero_estudiantes': len(estudiantes),
        'mititulo': 'listado de estudiantes y telefonos'
    }
    return render(request, 'listadoEstudiantesEjm.html', informacion_template)
