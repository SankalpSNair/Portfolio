from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email Address', 'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'class': 'form-control', 'rows': 10}),
        }
