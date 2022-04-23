from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):
    # username = forms.CharField()
    # password1 = forms.CharField()
    # password2 = forms.CharField()
    company_name = forms.CharField()

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'company_name')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'