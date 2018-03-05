from django import forms
from applicationlist.models import Application

class LoginForm(forms.Form):
    email = forms.CharField(label='AAU mail', max_length=255)
    password = forms.CharField(widget=forms.PasswordInput())

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
