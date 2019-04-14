from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from practice import daoapp

def index(request):
    session = request.session
    if 'role_id' in session.keys() and 'user_id' in session.keys():
        role_id = int(session['role_id'])
        ent_id = int(session['user_id'])
        menu = daoapp.getMenu(role_id=role_id)
        profile = daoapp.getProfile(role_id=role_id, user_id=ent_id)
        username = daoapp.getUsername(role_id, ent_id)
        return render(request, 'practice/index.html', {'menu': menu, 'information': profile, 'username': username,
                                                       'role_name': 'enterprise'})
    else:
        return redirect(reverse('practice:login'))

# 响应显示个人信息的请求
def profile(request):
    pass


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

