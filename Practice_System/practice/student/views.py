from django.http import HttpResponse
from django.shortcuts import render,reverse,redirect

from practice import daoapp


def index(request):
    session = request.session
    if 'role_id' in session.keys() and 'user_id' in session.keys():
        role_id = int(session['role_id'])
        stu_id = int(session['user_id'])
        menu = daoapp.getMenu(role_id=role_id)
        profile = daoapp.getProfile(role_id=role_id, user_id=stu_id)
        username = daoapp.getUsername(role_id, stu_id)
        return render(request, 'practice/index.html', {'menu': menu, 'information': profile, 'username': username})
    else:
        return redirect(reverse('practice:login'))


# 响应显示个人信息的请求
def profile(request):
    pass


# 响应显示岗位管理的请求
def postmanage(request):
    pass


# 响应显示岗位浏览的请求
def browsejobs(request):
    pass


# 响应显示已申请岗的请求
def applied(request):
    pass


# 响应显示协议管理的请求
def protocol(request):
    pass


# 响应显示实习协议的请求
def internship(request):
    pass


# 响应显示三方协议的请求
def tripartite(request):
    pass


# 响应显示就业协议的请求
def employment(request):
    pass


# 响应显示实习周记的请求
def weeklyreport(request):
    pass

# 响应显示新建周记的请求
def newreport(request):
    pass


# 响应显示已写周记的请求
def reporthistory(request):
    pass

