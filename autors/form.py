from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Autors



class AutorForm(ModelForm):
    
    class Meta:
        model = Autors
        fields = ['description']

