from django.forms import ModelForm
from .models import Tags
from django.core.exceptions import ValidationError

class TagsForm(ModelForm):
    class Meta:
        model = Tags
        fields = '__all__'
