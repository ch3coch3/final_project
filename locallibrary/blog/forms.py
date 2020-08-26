from django import forms
from .models import Post,Category

choices = Category.objects.all().values_list('name','name')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','category','content')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':choices}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'other':forms.TextInput(attrs={'class':'form-control','placeholder':'America'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choices ,attrs={'class':'form-control'}),
        }