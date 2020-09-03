from django import forms
from .models import Post,Comment,Category,Area
from blog.widget import RichTextBleachField

choices = [('Course reviews', 'Course reviews'), ('Daily life', 'Daily life'), ('Foods', 'Foods'), ('Entertainment', 'Entertainment'), 
            ('Laws', 'Laws'), ('Transportation', 'Transportation'), ('Customs,traditions', 'Customs,traditions'), ('Expenses', 'Expenses'), 
            ('Accommodation', 'Accommodation'), ('Travel', 'Travel'), ('School reviews', 'School reviews'), ('Climate', 'Climate'),
            ('other', 'other')]
choices_area = [('Americas', 'Americas'), ('Asia', 'Asia'), ('Europe', 'Europe'), ('Africa', 'Africa'), ('Oceania', 'Oceania')]

class PostForm(forms.ModelForm):
    # category = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=choices)
    tags = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=choices)
    class Meta:
        model = Post
        fields = ('title','area','tags','content')

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'other':forms.TextInput(attrs={'class':'form-control','placeholder':'America'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            # 'content':RichTextBleachField(),
            # 'category':forms.Select(choices=choices,attrs={'class':'form-control'}),
            # 'category':forms.CheckboxSelectMultiple(choices=choices,attrs={'class':'form-control'}),
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