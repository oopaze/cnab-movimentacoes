from django import forms


class MovimentacoesUploadForm(forms.Form):
    file = forms.FileField()