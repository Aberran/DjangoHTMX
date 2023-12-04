from django import forms
from .models import Karticka

class KartickaForm(forms.ModelForm):
    class Meta:
        model = Karticka
        fields = ('name', 'description', 'is_active')