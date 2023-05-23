from django import forms

class CreateLoginForm(forms.Form):
    email = forms.EmailField(max_length=30, required=True, label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=30, label='Password' ,widget=forms.PasswordInput(attrs={'class': 'form-control'}))
