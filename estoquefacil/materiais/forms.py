from django import forms
from .models import Materiais


class EntradaMateriais(forms.ModelForm):
    class Meta:
        model = Materiais
        fields = "__all__"
