from django import forms
from .models import musicanModel

class musicianForm(forms.ModelForm):
    class Meta:
        model = musicanModel
        fields = '__all__'
