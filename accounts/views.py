from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if len(username) != 0 or len(email) != 0 or len(password) != 0 or len(password2) != 0:
            if password == password2:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Это имя пользователя занято!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return redirect('login')
            else:
                messages.error(request, 'Пароли не совпадают')  
                return redirect('register')
        else:
            messages.error(request, 'Не все поля заполнены')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Неверные данные')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('index')
