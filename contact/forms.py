from django import forms
from django.forms import widgets
from .models import ContactForm


# class ContactForm(forms.Form):
# your_name = forms.CharField(widget=forms.TextInput(
#     attrs={'class': 'form-control', 'placeholder': 'Your name'}))
# your_email = forms.EmailField(
#     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}))
# subject = forms.CharField(widget=forms.TextInput(
#     attrs={'class': 'form-control', 'placeholder': 'Subject'}))
# message = forms.CharField(widget=forms.Textarea(
#     attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': 6, 'cols': 10}))

class NewContactForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ("your_name", "your_email", "subject", "message")
        widgets = {
            "your_name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            "your_email" : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}),
            "subject" : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            "message" : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': 6, 'cols': 10}),
        }
