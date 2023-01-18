from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegistrForm, LoginForm
from django.contrib import messages




def register(request):
    request.title = "Ro'yxatdan o'tish"
    if request.method == 'POST':
        form = RegistrForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Siz muvaffaqiyatli ro'yxatdan o'tdingiz.")
            return redirect('accaunts:login')
    else:
        form = RegistrForm()

    return render(request, 'accaunts/sign_up.html',{'form': form})


def user_login(request):
    request.title = "Tizimga kirish"
    form = LoginForm()
    if request.POST:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Xush kelibsiz!! {}'.format(user.first_name))
                return redirect('main:home')
            form.add_error('password', "Username va/yoki parol noto'g'ri. ")

    return render(request, 'accaunts/login.html', {
        'form': form
    })