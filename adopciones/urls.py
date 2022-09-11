from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('',views.inicio, name ='inicio'),
    path('galeria',views.galeria, name ='galeria'),
    path('nosotros', views.nosotros, name = 'nosotros'),
    path('publicar', views.publicar, name = 'publicar'),

    path('contenido/editar',views.editar, name='editar'),
    path('contenido/formulario', views.formulario, name='formulario'),
    path('contenido/index', views.index, name='index'),
    path('contenido/adoptar', views.adoptar, name='adoptar'),


    path('contenido/provisorio', views.provisorio, name='provisorio'),
    path('elimina<int:id>', views.eliminar, name='eliminar'),






    path('contenido/adoptar<int:id>', views.adoptar, name='adoptar'),

    path('contenido/provisorio<int:id>', views.provisorio, name='provisorio'),
    
    path('contenido/editar/<int:id>',views.editar, name='editar'),

    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
