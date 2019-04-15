from django.http import HttpResponse
from django.shortcuts import render,reverse,redirect

from practice import daoapp
from practice.models import Student
from Practice_System.settings import BASE_DIR

import os

def index(request):
    session = request.session
    # if 'role_id' in session.keys() and 'user_id' in session.keys():
    role_id = int(session['role_id'])
    stu_id = int(session['user_id'])
    menu = daoapp.getMenu(role_id=role_id)
    username = daoapp.getUsername(role_id, stu_id)
    information = daoapp.getInformations(role_id=role_id, user_id=stu_id)
    return render(request, 'practice/index.html', {'menu': menu, 'information': information, 'username': username,
                                                   'role_name': 'student'})


# 响应显示信息修改的请求
def profile(request):
    session = request.session
    role_id = int(session['role_id'])
    stu_id = int(session['user_id'])
    context = {}
    menu = daoapp.getMenu(role_id=role_id)
    username = daoapp.getUsername(role_id, stu_id)
    profile = daoapp.getProfile(role_id=role_id, user_id=stu_id)
    context = profile.copy()
    context['menu'] = menu
    context['username'] = username

    if request.method == 'GET':
        return render(request, 'practice/profilestudent.html', context )
    elif request.method == 'POST':
        password = request.POST['password']
        student = Student.objects.get(stu_id=stu_id)
        stu_pwd = student.stu_pwd
        # 判断是否有权限修改，（密码是否正确）
        if password != stu_pwd:
            context['error_message'] = '密码错误'
            return render(request, 'practice/profilestudent.html', context)
        student.stu_age = request.POST['age']
        student.phone_num = request.POST['phone']
        student.e_mail = request.POST['email']
        if request.POST.get('tripartite') == 'on':
            student.tripartite_agreement = True
        elif not request.POST.get('tripartite'):
            student.tripartite_agreement = False
        if request.POST.get('practice') == 'on':
            student.practice_agreement = True
        elif not request.POST.get('tripartite'):
            student.practice_agreement = False
        if request.POST.get('employment') == 'on':
            student.employment_agreement = True
        elif not request.POST.get('tripartite'):
            student.employment_agreement = False
        student.stu_class = request.POST['class']
        student.major = request.POST['major']
        student.address = request.POST['address']
        student.political_status = request.POST['politicalstatus']
        student.target_post = request.POST['targetpost']
        student.intention_area = request.POST['intentionarea']
        resumefile = request.FILES.get("resume", None)
        if resumefile:
            if __handle_uploaded_file(resumefile, 'media{}practice{}{}{}{}'.format(os.sep, os.sep, stu_id, os.sep, str(resumefile))):
                resume = 'practice/{}/{}'.format(stu_id, str(resumefile))
                student.resume = resume
        student.save()
        return redirect('practice.student:index')


def __handle_uploaded_file(file, url):
    path = os.path.join(BASE_DIR, url)
    dirname = os.path.dirname(path)
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    with open(os.path.join(BASE_DIR, url), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return True





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

