from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'checkout-first-name',
                'placeholder': 'First Name'
            }),
            'last_name': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'checkout-last-name',
                'placeholder': 'Last Name'
            }),
            'email': forms.EmailInput(attrs={
                'type': 'email',
                'class': 'form-control',
                'id': 'checkout-email',
                'placeholder': 'Email address'
            }),
            'phone': forms.TextInput(attrs={
                'type': 'text',
                'class': 'form-control',
                'id': 'checkout-phone',
                'placeholder': 'Phone'
            }),

        }

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email address',
            'phone': 'Phone'
        }
