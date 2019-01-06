from django.shortcuts import render, redirect
from django.http import HttpResponse
from authority import models as author_models
from authority.middleware.permission import initial_permission
from django.contrib.auth.models import auth


# Create your views here.


def user(request):
    user_id = request.session.get('user_id')
    user = author_models.UserInfo.objects.filter(id=user_id).first()
    queryset = {
        'user': user,
    }

    return render(request, 'user.html', queryset)


def users_add(request):
    return HttpResponse('users_add')


def users_edit(reqeust):
    return HttpResponse('users_edit')


def role(request):
    return render(request, 'role.html')


def role_add(request):
    return HttpResponse('role_add')


def login(request):
    if request.method == "POST":
        name = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user = auth.authenticate(username=name, password=pwd)
        if user:
            auth.login(request, user)
            # 注册权限和user_id
            initial_permission(user, request)
            return redirect('/user/')
    return render(request, 'login.html')
