from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from .forms import MensajeContactoForm, TransaccionForm
from .models import *


def index(request):
	testimonios= Testimonio.objects.all()	
	seminarios= Actividad.objects.all()	
	return render(request, 'paweb/index.html', {
		'testimonios': testimonios,
		'seminarios': seminarios,	
	})

def actividad(request, pk):
	actividad= get_object_or_404(Actividad, pk=pk) 
	return render(request, 'paweb/actividad.html', {
		'actividad': actividad,
	})

def contacto(request):
	base_template= 'paweb/partes/base.html'
	esta_mirando= 'contacto'
	if request.htmx:
		base_template= 'paweb/partes/base_para_embeber.html' 
		esta_mirando= request.htmx.current_url

	if request.method == 'POST': #A: nos mandaron los datos
		form = MensajeContactoForm(request.POST)
		if form.is_valid():
			mensaje= form.save(commit=False) #A: no guardar en la base de datos, asi lo modifico
			mensaje.texto= f'URL: {esta_mirando}\n{mensaje.texto}'
			mensaje.save() #A: ahora que le agregue la URL si lo guardo en la DB
			return render(request, 'paweb/partes/contacto/resultado.html')
	else: #A: 1ra vez, pide el form vacio
		form = MensajeContactoForm()

	return render(request, 'paweb/partes/contacto/formulario.html', {
		'base_template': base_template,
		'form': form
	})

def billetera(request):
	return render(request, 'paweb/billetera.html', {
	})

#VER: https://docs.djangoproject.com/en/4.1/topics/pagination/#using-paginator-in-a-view-function

def tienda(request):
	avisos = Aviso.objects.all() #traer todos los avisos
	paginator = Paginator(avisos, 6) # Muestra n avisos por página
	page_number = request.GET.get('page')
	pagina_avisos = paginator.get_page(page_number)
	return render(request, 'paweb/tienda.html', {
		'avisos': pagina_avisos, 
		'paginas': range(1,5) #TODO: usar página actual y máximo de paginador
	})

def historial(request):
	return render(request, 'paweb/historial.html', {
	})


def transaccion(request):
	base_template= 'paweb/partes/base.html'
	esta_mirando= 'catalogo' #U: qué página está mirando
	if request.htmx:
		base_template= 'paweb/partes/base_para_embeber.html' 
		esta_mirando= request.htmx.current_url

	if request.method == 'POST': #A: nos mandaron los datos
		form = TransaccionForm(request.POST)
		if form.is_valid():
			transaccion= form.save(commit=False) #A:
			transaccion.save() #A: ahora que le agregue la URL si lo guardo en la DB
			return render(request, 'paweb/partes/transaccion/resultado.html')
	else: #A: 1ra vez, pide el form vacio
		form = TransaccionForm(request.GET) #A: usar valores que vengan en la URL

	return render(request, 'paweb/partes/transaccion/formulario.html', {
		'base_template': base_template,
		'form': form
	})