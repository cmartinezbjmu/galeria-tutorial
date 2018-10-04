from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Imagen, ImageForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    lista_imagenes = Imagen.objects.all()
    context = {'lista_imagenes': lista_imagenes}
    return render(request, 'polls/index.html', context)

def add_image(request):
    if request.method == 'POST': #Si el usuario está enviando el formulario con datos
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # Guardar los datos en la base de datos

            return HttpResponseRedirect(reverse('images:index'))
    else:
        form = ImageForm()

    return render(request, 'polls/image_form.html', {'form': form})