"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views
from . import views1


urlpatterns = [
        path('', views.index, name='index'),
        path('listado-estudiantes', views.listadoEstudiantes,
            name='listadoEstudiates'),
        path('listado/estudiantes/dos', views.listadoEstudiantesDos,
            name='listadoEstudiatesDos'),
        path('listado/estudiantes/nuevo', views1.listado_nuevo,
            name='listadoNuevo'),
        path('listado/estudiantes/tres', views.listadoEstudiantes,
             name='listadoEstudiantesTres'),

 ]

