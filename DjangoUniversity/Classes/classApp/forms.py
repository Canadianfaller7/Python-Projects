from django.forms import ModelForm
from .models import djangoClasse

class ClassForm(ModelForm):
    class Meta:
        model = djangoClasse
        fields = '__all__'