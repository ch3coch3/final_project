from django import forms
# from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import User

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
    username = forms.CharField(label='帳號',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='密碼',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='確認密碼',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='電子郵件',widget=forms.EmailInput(attrs={'class':'form-control'}))
    identicate = forms.ImageField(label='學生證',widget=forms.FileInput)
    image = forms.ImageField(label='大頭貼',widget=forms.FileInput,required=False)
    gender = forms.ChoiceField(label='性別',widget=forms.Select(attrs={'class':'form-control'}),choices=gender_choice)
    identication = forms.MultipleChoiceField(label='身分別',widget=forms.CheckboxSelectMultiple,choices=id_choice)
    class Meta:
        model = User
        fields = ['username','password','password2','email','identicate','image','gender','identication']


    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError('密碼不相符')
        return password2
    def save(self):
        user = super().save(commit=False)   # 暫不儲存
        user.set_password(user.password)
        user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','image']

# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['image']
