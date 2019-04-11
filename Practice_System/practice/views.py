from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import Teacher,Enterprise,Student


# Create your views here.
def index(request):
    session = request.session
    menu = {
        '企业信息': {
            '信息查看': 'enterprise/review/',
            '信息修改': 'enterprise/update/',
        },
        '招聘管理': {
            '岗位公开': 'enterprise/review/',
            '审核简历': 'enterprise/update/',
            '岗位公开1': 'enterprise/review/',
            '审核简历2': 'enterprise/update/',
        },
        '实习生考核': {
            '实习生': 'enterprise/review/',
            '实习生记录': 'enterprise/update/',
            '嘻嘻嘻': 'enterprise/review/',
            '哈哈哈': 'enterprise/update/',
        },
        '登录成功的user的id': {
            str(session['username']) : '{% url "practice:student" {{ '+ str(session['username']) + ' }}%}',
        },
    }
    return render(request, 'practice/index.html', {'menu':menu})

def login(request):
    return render(request, 'practice/login.html')


def dologin(request):
    session = request.session
    username = request.POST['username']
    password = request.POST['password']
    user = Student.objects.all() #从数据库中拿出所有student
    print(user[0].stu_id)
    print(user[0].stu_pwd)
    #判断账号密码是否匹配
    if int(username) == user[0].stu_id and password == user[0].stu_pwd:
        #把登录成功的用户id存到session中  key: username  value: stu_id
        session['username'] = user[0].stu_id
        return redirect(reverse('practice:index'))
    else:
        return redirect(reverse('practice:login'))
    # return render(request, 'practice/index.html')

