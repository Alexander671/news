from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import DraftsModel



class DraftsForm(ModelForm):
    
    class Meta:
        model = DraftsModel
        fields = ['text', 'images']