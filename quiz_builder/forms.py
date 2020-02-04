from django import forms


class ItemsForm(forms.Form):
    items = forms.CharField()
