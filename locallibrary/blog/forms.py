from django import forms
from .models import Post,Comment,Category,Area

choices = Category.objects.all().values_list('name','name')
choices_area = Area.objects.all().values_list('where','where')



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','area','category','content')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'other':forms.TextInput(attrs={'class':'form-control','placeholder':'America'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choices,attrs={'class':'form-control'}),
            'area':forms.Select(choices=choices_area,attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
            'name':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }