from django import forms


class LoginForm(forms.Form):
   login = forms.CharField(label="Login", max_length=30)
   password = form.CharField(label="Haslo", widget=forms.PasswordInput)
