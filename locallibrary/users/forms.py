from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

gender_choice = [
    ('1','男'),
    ('2','女'),
    ('3','第三性'),
    ]
id_choice = [
    ('1','交換生'),
    ('2','學伴'),
    ('3','外籍生'),
    ('4','過去有超過兩個月的出國經驗，非學校活動'),
]
class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='使用者名稱')
    password = forms.CharField(label='密碼')
    password2 = forms.CharField(label='確認密碼')
    email = forms.EmailField(label='電子郵件')
    # ID = forms.ImageField(label='上傳學生證或入學證明',default='default.jpg',upload_to='profile_pics')
    # picture = forms.ImageField(label='上傳大頭貼照',default='default.jpg',upload_to='profile_pics')
    gender = forms.ChoiceField(label='性別',choices=gender_choice)
    identication = forms.MultipleChoiceField(label='身分別',choices=id_choice)
    class Meta:
        model = User
        fields = ['username','password','password2','email','gender','identication']
    
    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError('密碼不相符')
        return password2
    def save(self):
        user = super().save(commit=False)
        user.set_password(user.password)
        user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        field = 'image'
