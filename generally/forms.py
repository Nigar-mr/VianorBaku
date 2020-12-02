from django import forms
from .models import LetterEmail


class LetterEForm(forms.ModelForm):
    class Meta:
        model = LetterEmail
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'name': 'NewsLetter',
                'type': 'text',
                'class': 'footer-newsletter__form-input',
                'id': 'footer-newsletter-address',
                'placeholder': 'Email Address...',
            })
        }
