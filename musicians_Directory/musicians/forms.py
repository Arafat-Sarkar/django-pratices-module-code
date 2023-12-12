from django import forms
from .models import Musican

class addForm(forms.ModelForm):
    class Meta:
        model = Musican
        fields = '__all__'