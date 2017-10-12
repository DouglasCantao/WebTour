from django.forms import ModelForm
from webtoursite.models import Onibus

class OnibusForm(ModelForm):
	class Meta:
		model = Onibus
		exclude = []