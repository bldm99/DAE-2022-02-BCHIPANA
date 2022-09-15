
from django.urls import path

from . import views
app_name = 'recetas'

urlpatterns = [
    # ex: /recetas/
    path('' ,views.index,name='index'),      #index en referencia al funcio en el archivo views y name es un alias
    # ex: /encuesta/5/
    #path('<int:pregunta_id>/' , views.detalle , name='detalle'),
    #path('<int:pregunta_id>/votar' , views.votar , name='votar')

]