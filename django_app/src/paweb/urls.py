from django.urls import path
from . import views

urlpatterns= [
	path('', views.index, name='index'),
	path('seminario/<int:pk>', views.actividad, name='actividad'),
	path('contacto', views.contacto, name='contacto'),
]
