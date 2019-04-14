from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse

from practice import daoapp


# 响应显示主页的请求
def index(request):
    session = request.session
    if 'role_id' in session.keys() and 'user_id' in session.keys():
        role_id = int(session['role_id'])
        tea_id = int(session['user_id'])
        menu = daoapp.getMenu(role_id=role_id)
        profile = daoapp.getProfile(role_id=role_id, user_id=tea_id)
        username = daoapp.getUsername(role_id, tea_id)
        return render(request, 'practice/index.html', {'menu': menu, 'information': profile, 'username': username,
                                                       'role_name': 'teacher'})
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


# 响应显示学生管理的请求
def studentmanage(request):
    pass


# 响应显示浏览简历的请求
def browseweeklyreport(request):
    pass


# 响应显示未读（周报）的请求
def unread(request):
    pass


# 响应显示已读（周报）的请求
def readed(request):
    pass

