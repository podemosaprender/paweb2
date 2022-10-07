from django.utils.translation import gettext_lazy as _

from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.contrib.auth import get_user_model

#from .models_extra import * #A: para que agregue otros lookups como like 
#from .util import *

import datetime as dt
import re
import hashlib

import logging
logger = logging.getLogger(__name__)

User= get_user_model() #U: la implementacion q este configurada

class MensajeContacto(models.Model): #U: cualquier texto que publiquemos, despues especializamos
	class Meta:
		verbose_name_plural = "MensajesContacto"

	fh_creado= models.DateTimeField(default=timezone.now)
	de_mail= models.EmailField(_('e-mail'))
	de_cel= PhoneNumberField(_('teléfono'),blank= True)
	titulo= models.CharField(_('asunto'),max_length=200)
	texto= models.TextField(_('mensaje'))

	def __str__(self):
		return f'{self.fh_creado} {self.de_mail} {self.titulo}'

class Actividad(models.Model): #U: seminario, grupo, etc.
	class Meta:
		verbose_name_plural = "Actividades"

	fh_creado= models.DateTimeField(default=timezone.now)
	titulo= models.CharField(max_length=200)
	hashtags= models.CharField(max_length=200)
	texto= models.TextField()
	estilo= models.CharField(max_length=200)

	def __str__(self):
		return f'{self.titulo} {self.hashtags}'

class Testimonio(models.Model): #U: Testimonio en el index
	class Meta:
		verbose_name_plural = "Testimonios"

	fh_creado= models.DateTimeField(default=timezone.now)
	de_quien= models.CharField(_('de_quien'), max_length=40)
	texto= models.TextField(_('texto'), max_length=300)

	def __str__(self):
		return f'{self.fh_creado} {self.de_quien} {self.texto[0:15]}'	


class Aviso(models.Model): #U: Aviso en el index
	class Meta:
		verbose_name_plural = "Avisos"

	fh_creado= models.DateTimeField(default=timezone.now)
	de_quien= models.CharField(_('de_quien'), max_length=40)
	titulo= models.CharField(_('titulo'), max_length=40)
	texto= models.TextField(_('texto'), max_length=300)
	cuanto= models.IntegerField(_('cuanto'))
	categorias= models.CharField(_('categorias'), max_length=200)

	def __str__(self):
		return f'{self.fh_creado} {self.de_quien} {self.texto[0:15]}'	


class Transaccion(models.Model): #U: Transacciones
	class Meta:
		verbose_name_plural = "Transacciones"

	fh_creado= models.DateTimeField(default=timezone.now)
	de_quien= models.CharField(_('de_quien'), max_length=40)
	a_quien= models.CharField(_('a_quien'), max_length=40)
	por= models.CharField(_('por'), max_length=200)
	cuanto= models.IntegerField(_('cuanto'))
	id= models.CharField(_('id'), max_length=5, primary_key=True)
	

	def __str__(self):
		return f'{self.fh_creado} {self.de_quien} -> {self.a_quien} {self.cuanto} {self.por[0:15]} '	