from django import forms

class NameForm(forms.Form):
    result = forms.CharField(label='Result', max_length=1000, widget=forms.Textarea)
