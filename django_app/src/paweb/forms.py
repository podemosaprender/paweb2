from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

from .models import MensajeContacto

def ReCaptchaF():
	f= ReCaptchaField(widget=ReCaptchaV3(attrs={'input_type':'hidden'}))
	return f

class MensajeContactoForm(forms.ModelForm):
	captcha = ReCaptchaF()

	class Meta:
		model= MensajeContacto
		fields= '__all__'
		exclude=('fh_creado',)

