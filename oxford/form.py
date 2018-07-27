from django import forms
from django.contrib.auth.models import User
class Myform(forms.Form):
    Word=forms.TextField(label='Enter the Word',max_length=300,)

