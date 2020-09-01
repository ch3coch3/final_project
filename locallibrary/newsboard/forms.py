from django import forms
from .models import Newsarticle

class Articleform(forms.ModelForm):
    class Meta:
        model = Newsarticle
        fields = ('title','body')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'other':forms.TextInput(attrs={'class':'form-control','placeholder':'America'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }
