from django import forms

class NameForm(forms.Form):
    text = forms.CharField(label='Result', max_length=1000)

