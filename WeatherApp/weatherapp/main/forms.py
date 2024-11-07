from .models import City
from django.forms import ModelForm, TextInput

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name' : TextInput(attrs={
            'class' : 'input_form',
            'id' : 'city',
            'placeholder' : 'Find a city...'
            })}