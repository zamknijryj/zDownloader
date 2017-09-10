from django import forms


class CdaForm(forms.Form):
    url = forms.CharField(label='',
                          widget=forms.TextInput(attrs={'placeholder': 'Link do filmu'}))
