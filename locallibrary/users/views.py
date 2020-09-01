from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

# 處理註冊
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('users:login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})

# 處理登入
def login(request):
    template = 'users/login.html'
    if request.method == 'GET':
        return render(request,template)
    
    # POST
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not username or not password:
        messages.error(request,'請填資料')
        return render(request,template)
    
    user = authenticate(username=username, password=password)
    if not user:
        messages.error(request,'登入失敗')
        return render(request,template)
    # login success
    auth_login(request,user)
    messages.success(request,'登入成功')
    return redirect('blog-home')

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,request.FILES,instance=request.user)
        # p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user)
        if u_form.is_valid():
            u_form.save()
            # p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:  
        u_form = UserUpdateForm(instance=request.user)
        # p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form':u_form,
        # 'p_form':p_form
        
    }
    return render(request, 'users/profile.html',context)