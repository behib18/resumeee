from django import forms


class ContactForm(forms.Form):
    your_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Your name'}))
    your_email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}))
    subject = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': 6, 'cols': 10}))
