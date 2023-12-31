from django import forms
from .models import ClientType,Client,Product,Order


class ClientInfo(forms.ModelForm):
    class Meta:
        model=Client
        fields="__all__"



