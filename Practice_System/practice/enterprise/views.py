from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from practice import daoapp
from practice.models import Enterprise


def index(request):
    session = request.session
    if 'role_id' in session.keys() and 'user_id' in session.keys():
        role_id = int(session['role_id'])
        ent_id = int(session['user_id'])
        menu = daoapp.getMenu(role_id=role_id)
        informations = daoapp.getInformations(role_id=role_id, user_id=ent_id)
        username = daoapp.getUsername(role_id, ent_id)
        return render(request, 'practice/index.html', {'menu': menu, 'information': informations, 'username': username,
                                                       'role_name': 'enterprise'})
    else:
        return redirect(reverse('practice:login'))

# 响应显示个人信息的请求
def profile(request):
    session = request.session
    role_id = int(session['role_id'])
    ent_id = int(session['user_id'])
    context = {}
    menu = daoapp.getMenu(role_id=role_id)
    username = daoapp.getUsername(role_id, ent_id)
    profile = daoapp.getProfile(role_id=role_id, user_id=ent_id)
    context = profile.copy()
    context['menu'] = menu
    context['username'] = username
    print(context)
    if request.method == 'GET':
        return render(request, 'practice/profileenterprise.html', context)
    elif request.method == 'POST':
        password = request.POST['password']
        enterprise = Enterprise.objects.get(ent_id=ent_id)
        ent_pwd = enterprise.ent_pwd
        # 判断是否有权限修改，（密码是否正确）
        if password != ent_pwd:
            context['error_message'] = '密码错误'
            return render(request, 'practice/profileenterprise.html', context)
        enterprise.ent_name = request.POST['ent_name']
        enterprise.introduction = request.POST['introduction']
        enterprise.ent_address = request.POST['address']
        enterprise.ent_phone = request.POST['phone']
        enterprise.ent_email = request.POST['email']
        enterprise.principal = request.POST['principal']
        enterprise.save()
        return redirect('practice.enterprise:index')


# 响应显示发布岗位的请求
def postjobs(request):
    pass


# 响应显示简历筛选的请求
def resumescreening(request):
    pass


# 响应显示已收（简历）的请求
def received(request):
    pass


# 响应显示已选（简历）的请求
def selected(request):
    pass


# 响应显示实习生管理的请求
def internmanage(request):
    pass

