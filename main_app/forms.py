from django.forms import ModelForm
from .models import Inspect

class InspectForm(ModelForm):
    class Meta:
        model = Inspect
        fields = ['date', 'condition']