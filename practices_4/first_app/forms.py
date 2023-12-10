from django import forms
from django.forms.widgets import NumberInput
import datetime
from first_app.models import modelForm



BIRTH_YEAR_CHOICES = ['1970', '1991', '1992']


class djagoFrom(forms.Form):
    name = forms.CharField()
    email = forms.EmailField( required = False,)
    comment = forms.CharField(widget=forms.Textarea)
    comment2 = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    agree = forms.BooleanField(initial=True)
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    message = forms.CharField(max_length = 10,)
    email_address = forms.EmailField( 
    label="Please enter your email address",)
    first_name = forms.CharField(initial='Your name')
    day = forms.DateField(initial=datetime.date.today)
    FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color_select = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors_pick = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
   
class listForm(forms.ModelForm):
    class Meta:
        model = modelForm
        fields = '__all__' 
    
  