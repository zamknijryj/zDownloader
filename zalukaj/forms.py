from django import forms


class ZalukajForm(forms.Form):
    url = forms.CharField(label='',
                          widget=forms.TextInput(attrs={'placeholder': 'Link do filmu'}))
