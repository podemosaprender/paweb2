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

	
