from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse

from practice import daoapp
from practice.models import Teacher,Job


# 响应显示主页的请求
def index(request):
    session = request.session
    if 'role_id' in session.keys() and 'user_id' in session.keys():
        role_id = int(session['role_id'])
        tea_id = int(session['user_id'])
        menu = daoapp.getMenu(role_id=role_id)
        informations = daoapp.getInformations(role_id=role_id, user_id=tea_id)
        username = daoapp.getUsername(role_id, tea_id)
        return render(request, 'practice/index.html', {'menu': menu, 'information': informations, 'username': username,
                                                       'role_name': 'teacher'})
    else:
        return redirect(reverse('practice:login'))


# 响应显示信息信息修改的请求
def profile(request):
    session = request.session
    role_id = int(session['role_id'])
    tea_id = int(session['user_id'])
    context = {}
    menu = daoapp.getMenu(role_id=role_id)
    username = daoapp.getUsername(role_id, tea_id)
    profile = daoapp.getProfile(role_id=role_id, user_id=tea_id)
    context = profile.copy()
    context['menu'] = menu
    context['username'] = username
    if request.method == 'GET':
        return render(request, 'practice/profileteacher.html', context)
    elif request.method == 'POST':
        password = request.POST['password']
        teacher = Teacher.objects.get(tea_id=tea_id)
        tea_pwd = teacher.tea_pwd
        # 判断是否有权限修改，（密码是否正确）
        if password != tea_pwd:
            context['error_message'] = '密码错误'
            return render(request, 'practice/profileteacher.html', context)
        teacher.tea_phone = request.POST['phone']
        teacher.tea_email = request.POST['email']
        teacher.college = request.POST['college']
        teacher.tea_post = request.POST['post']
        teacher.save()
        return redirect('practice.teacher:index')


# 响应显示岗位浏览的请求
def browsejobs(request):
    session = request.session
    role_id = int(session['role_id'])
    tea_id = int(session['user_id'])
    context = {}
    context['menu'] = daoapp.getMenu(role_id=role_id)
    context['username'] = daoapp.getUsername(role_id, tea_id)
    jobs = Job.objects.all()
    context['jobs'] = jobs
    context['role_name'] = 'teacher'
    return render(request, 'practice/browsejobs.html', context)


# 响应显示岗位详情的请求
def showjob(request, job_id):
    job = Job.objects.get(job_id=job_id)
    return render(request, 'practice/showjob.html', {'job': job})


# 响应显示企业详情的请求
def information(request, ent_id):
    session = request.session
    role_id = int(session['role_id'])
    tea_id = int(session['user_id'])
    menu = daoapp.getMenu(role_id=role_id)
    username = daoapp.getUsername(role_id, tea_id)
    information = daoapp.getInformations(role_id=3, user_id=ent_id) # 企业的详细信息
    return render(request, 'practice/index.html', {'menu': menu, 'information': information, 'username': username,
                                                   'role_name': 'teacher'})



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

