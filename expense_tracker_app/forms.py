from django import forms
from . models import Transactions

class Transactions_form(forms.ModelForm):
    
    class Meta:
        model = Transactions
        fields = ['date', 'title', 'category', 'type', 'amount',]
        
        widgets = {
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Grocery shopping'
            }),
            'category': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Food, Travel, Bills'
            }),
            'type': forms.Select(attrs={
                'class': 'form-select'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter amount'
            }),
           
        }