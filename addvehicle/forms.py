from cProfile import label
from django import forms
from . models import Vechicle
class Vechicleform(forms.ModelForm):    
    class Meta:
        model =  Vechicle
        fields = ['name' , 'speed', 'avgspeed', 'fuellev', 'enginestat', 'temp']
        labels = {'name': ' Vechicle name', 'speed':'Speed (km/hr)','avgspeed': 'Average speed(km/hr)', 'fuellev': 'Fuel level (%)', 'enginestat': 'Engine Status','temp':'Temperature (°C)' }
        widgets = {
        'name' : forms.TextInput(attrs={'class': 'form-control'}),
        'speed': forms.NumberInput(attrs={'class': 'form-control'}),
        'avgspeed':forms.NumberInput(attrs={'class': 'form-control'}),
        'fuellev':forms.NumberInput(attrs={'class': 'form-control'}), 
        'enginestat':forms.TextInput(attrs={'class': 'form-control'}), 
        'temp':forms.NumberInput(attrs={'class': 'form-control'}),
        }
