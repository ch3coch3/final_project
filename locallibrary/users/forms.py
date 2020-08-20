from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=gender_choice)
    identication = forms.MultipleChoiceField(choices=id_choice)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']