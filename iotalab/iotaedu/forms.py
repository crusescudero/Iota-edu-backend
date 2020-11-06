from django import forms

class ContactForm(forms.Form):
  Nombre = forms.CharField(required=True)
  Email = forms.EmailField(required=True)
  Telefono = forms.CharField(required=True)
  Mensaje = forms.CharField(required=True)

class CreateUser(forms.Form):
  Nombre = forms.CharField(required=True)
  Email = forms.EmailField(required=True)
  Contraseña = forms.CharField(max_length=20, widget=forms.PasswordInput)

class LoginUserForm(forms.Form):
  username = forms.CharField(required=True)
  password = forms.CharField(max_length=20, widget=forms.PasswordInput)