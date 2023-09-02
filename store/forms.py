# forms.py

from django import forms


class MyForm(forms.Form):
    
    field1 = forms.IntegerField(label='Field 1')
    field2 = forms.IntegerField(label='Field 2')
