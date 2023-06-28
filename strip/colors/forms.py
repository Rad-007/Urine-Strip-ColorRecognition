from django import forms
from .models import StripImage

class StripImageForm(forms.ModelForm):
    class Meta:
        model = StripImage
        fields = ('image',)
