from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder' : 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'last Name'}))


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted small">Required</span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li> check password</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted small">Password must match</span>'


class AddRecordForm(forms.ModelForm):
    first_name = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'First Name'}))
    last_name = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'Last Name'}))
    email = forms.EmailField(required=True, max_length=50, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder' : 'email'}))
    phone = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'phone'}))
    address = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'address'}))
    city = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'city'}))
    state = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'state'}))
    zipcode = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder' : 'zipcode'}))

    class Meta:
        model = Record
        exclude = ("user",) #will add all