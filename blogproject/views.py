from django.contrib.auth import authenticate
from django.contrib.auth import login as user_login
from django.shortcuts import HttpResponse, render, redirect, render_to_response

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        if user:
            user_login(request, user)
            message = '认证成功'
            return render(request, 'login.html', {"message": message})
        else:
            message = '认证失败'
            return render(request, 'login.html', {"message": message})
    return render(request, 'login.html')