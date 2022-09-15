from django.shortcuts import render

from select import select
from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Autor , Receta ,Comentario
# Create your views here.

#---------------------------para vista index-------------------
def index(request):
    latest_question_list = Receta.objects.order_by('-pub_date')[:5] #llamado a la tabla Receta /[:5] es el numero
    context = {                                                       # de recetas que va a traer
        'latest_question_list': latest_question_list
    }
    return render(request, 'receta/index.html', context)