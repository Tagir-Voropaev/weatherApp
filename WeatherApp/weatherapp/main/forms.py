from .models import search_cityModel
from django.forms import ModelForm, TextInput


class search_city(ModelForm):
    class Meta():
        model = search_cityModel
        fields = ['city_name_form']
        widgets = {'city_name_form' : TextInput(attrs={
            'class' : "input_form", 
            'name' : "city_searching", 
            'placeholder' : "Find the city"
            })}
        # city_name_form = forms.CharField(max_length=50 )