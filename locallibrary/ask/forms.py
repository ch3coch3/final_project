from django import forms
from .models import Askpost,AskComment

class PostForm(forms.ModelForm):
    class Meta:
        model = Askpost
        fields = ('title','content')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = AskComment
        fields = ('body',)
        widgets = {
            'user':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }