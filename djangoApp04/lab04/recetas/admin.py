from django.contrib import admin

# Register your models here.
from.models import Autor , Receta , Comentario  #Importamos todas las clases creadas em models

admin.site.register(Autor)
admin.site.register(Receta)
admin.site.register(Comentario)