from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login
import HTMLTestRunner
import pymysql
# Create your views here.


def logout(request):
    auth.logout(request)
    return render(request,'index.html')
def login(request):
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            request.session['user'] = username
            reponse = HttpResponseRedirect('Login')
        else:
            return render(request,'Login.vue',{'error':'username or password erro'})
    # else:
    #     context = {}
    #     return render(request,'login.html',context)

    return render(request,'Login.vue')