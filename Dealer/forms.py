from .models import Vehiculos
from django import forms

class taskform(forms.ModelForm): 
    class Meta: 
        model = Vehiculos
        fields = ['name', 'model', 'year', 'price', 'quantity', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}), 
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Model'}),
            'year': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Year'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price'}), 
            'quantity': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quantity'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }