from django.shortcuts import render,redirect,reverse
from django.contrib import auth

from .models import Teacher,Enterprise,Student

role = {1: 'admin', 2: 'teacher', 3: 'enterprise', 4: 'student'}


# Create your views here.
#进入首页
def index(request):
    session = request.session
    role_id = int(session['role_id'])
    if role_id in [1, 2, 3, 4]:
        return redirect(reverse('practice.' + role[role_id] +':index'))
    else:
        return redirect(reverse('practice:login'))


#响应登陆操作，登陆成功就重定向到首页
def login(request):
    session = request.session
    if request.method == 'GET':
        return render(request, 'practice/login.html')
    try:
        role_id = int(request.POST['role_id'])
        user_id = int(request.POST['username'])
    except:
        return render(request,'practice/login.html', {'error_message': '用户名只能为数字'})
    user_pwd = str(request.POST['password'])
    if role_id == 2:    #如果是以老师身份登录，则从Teacher中查找，tea_id与user_id相等的一条teacher的数据
        try:
            user = Teacher.objects.get(tea_id=user_id)
        except Teacher.DoesNotExist:
            return render(request,'practice/login.html', {'error_message': '用户名或密码错误'})
        else:
            password = user.tea_pwd     #取出密码
    elif role_id == 3:  #如果是以企业身份登录，Enterprise，ent_id与user_id相等的一条enterprise的数据
        try:
            user = Enterprise.objects.get(ent_id=user_id)
        except Enterprise.DoesNotExist:
            return render(request,'practice/login.html', {'error_message': '用户名或密码错误'})
        else:
            password = user.ent_pwd
    elif role_id == 4:  #如果是以学生身份登录，则从Student中查找，stu_id与user_id相等的一条student的数据
        try:
            user = Student.objects.get(stu_id=user_id)
        except Student.DoesNotExist:
            return render(request,'practice/login.html', {'error_message': '用户名或密码错误'})
        else:
            password = user.stu_pwd
    if user is not None and user_pwd == password:       #登录成功
        session['role_id'] = role_id
        session['user_id'] = user_id
        return redirect(reverse('practice.' + role[role_id] +':index'))
    else:
        return redirect(reverse('practice:login'), {'error_message': '用户名或密码错误'})


#退出登录操作，重定向到登陆页面
def logout(request):
    auth.logout(request)
    return redirect(reverse('practice:login'))
