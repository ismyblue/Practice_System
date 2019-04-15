from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from practice import daoapp
from practice.models import Enterprise,Job, Choice


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


# 响应显示信息修改的请求
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
    context['role_name'] = 'enterprise'
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
    session = request.session
    role_id = int(session['role_id'])
    ent_id = int(session['user_id'])
    context = {}
    menu = daoapp.getMenu(role_id=role_id)
    username = daoapp.getUsername(role_id, ent_id)
    jobs = daoapp.getJobs(ent_id)
    context['menu'] = menu
    context['username'] = username
    context['role_name'] = 'enterprise'
    context['jobs'] = jobs
    return render(request, 'practice/jobslist.html', context)


# 响应增加岗位请求
def addjob(request):
    session = request.session
    ent_id = int(session['user_id'])
    if request.method == 'GET':
        return render(request, 'practice/addjob.html')
    elif request.method == 'POST':
        job_name = request.POST['job_name']
        job_desc = request.POST['job_desc']
        employ_num = request.POST['employ_num']
        salary = request.POST['salary']
        job_time = request.POST['job_time']
        enterprise = Enterprise.objects.get(ent_id=ent_id)
        job = Job(ent_id=enterprise, job_name=job_name, job_desc=job_desc, employ_num=employ_num, salary=salary, job_time=job_time )
        job.save()
        return HttpResponse('success')

# 响应显示岗位的请求
def showjob(request, job_id):
    job = Job.objects.get(job_id=job_id)
    return render(request, 'practice/showjob.html', {'job': job})


# 响应更新岗位的请求
def updatejob(request, job_id):
    session = request.session
    ent_id = int(session['user_id'])
    job = Job.objects.get(job_id=job_id)
    if request.method == 'GET':
        return render(request, 'practice/updatejob.html', {'job': job})
    elif request.method == 'POST':
        job.job_name = request.POST['job_name']
        job.job_desc = request.POST['job_desc']
        job.employ_num = request.POST['employ_num']
        job.salary = request.POST['salary']
        job.job_time = request.POST['job_time']
        job.enterprise = Enterprise.objects.get(ent_id=ent_id)
        job.save()
        return HttpResponse('success')


# 响应删除岗位的请求：
def deletejob(request, job_id):
    ent_id = int(request.session['user_id'])
    job = Job.objects.get(job_id=job_id)
    if ent_id != job.ent_id.ent_id:
        render(request, 'practice/error.html', {'error_message': '您没有权限！'})
    job.delete()
    return HttpResponse('success')


# 响应显示已收（简历）的请求
def received(request):
    role_id = request.session['role_id']
    ent_id = request.session['user_id']
    enterprise = Enterprise.objects.get(ent_id=ent_id)
    jobs = Job.objects.filter(ent_id=enterprise)
    choices = []
    for job in jobs:
        choices += Choice.objects.filter(job_id=job).exclude(result=True)
    context = {}
    context['choices'] = choices
    context['menu'] = daoapp.getMenu(role_id=role_id)
    context['username'] = daoapp.getUsername(role_id, ent_id)
    context['role_name'] = 'enterprise'
    return render(request, 'practice/received.html', context)


# 响应显示学生详情的请求
def information(request, stu_id):
    session = request.session
    role_id = int(session['role_id'])
    ent_id = int(session['user_id'])
    menu = daoapp.getMenu(role_id=role_id)
    username = daoapp.getUsername(role_id, ent_id)
    information = daoapp.getInformations(role_id=4, user_id=stu_id)  # 学生的详细信息
    return render(request, 'practice/index.html', {'menu': menu, 'information': information, 'username': username,
                                                   'role_name': 'enterprise'})


# 响应选择学生的请求
def select(request, job_id, stu_id):
    choice = Choice.objects.get(job_id=job_id, stu_id=stu_id)
    if choice.job_id.ent_id.ent_id == request.session['user_id']:
        choice.result = True
        choice.save()
        return redirect(reverse('practice.enterprise:selected'))
    else:
       return render(request, 'practice/error.html', {'error_message': '没有权限'})



# 响应删除学生的请求
def deletechoice(request, job_id, stu_id):
    choice = Choice.objects.get(job_id=job_id, stu_id=stu_id)
    if choice.job_id.ent_id.ent_id == request.session['user_id']:
        choice.delete()
        return HttpResponse('success')
    else:
        return render(request, 'practice/error.html', {'error_message': '没有权限'})


# 响应显示已选（简历）的请求
def selected(request):
    role_id = request.session['role_id']
    ent_id = request.session['user_id']
    enterprise = Enterprise.objects.get(ent_id=ent_id)
    jobs = Job.objects.filter(ent_id=enterprise)
    choices = []
    for job in jobs:
        choices += Choice.objects.filter(job_id=job, result=True)
    context = {}
    context['choices'] = choices
    context['menu'] = daoapp.getMenu(role_id=role_id)
    context['username'] = daoapp.getUsername(role_id, ent_id)
    context['role_name'] = 'enterprise'
    return render(request, 'practice/received.html', context)


# 响应显示实习生管理的请求
def internmanage(request):
    pass

