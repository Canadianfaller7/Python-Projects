from django.forms import ModelForm
from .models import djangoClasse
# this will connect with our models.py so like for the type, name, description and etc. These will all become a field
# on the website where the user will put in the information and then with this productForm class we can get all
# that information at once and then get what we need from it
class ClassForm(ModelForm):
    class Meta:
        model = djangoClasse
        fields = '__all__' # this is a dunder and a shortcut to get all the fields from the models.py