from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(label="your name", max_length=64)
    age = forms.IntegerField(label="your age")
    favorite_book = forms.CharField(label="your favorite book", max_length=255)
