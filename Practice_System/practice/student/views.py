from django.http import HttpResponse
from django.shortcuts import render,reverse,redirect


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
    }
    if 'role_id' in session.keys() and 'user_id' in session.keys():
        menu['登录成功的user的id'] = {
            session['role_id'] : session['role_id'],
            session['user_id'] : session['user_id'],
        }
        return render(request, 'practice/index.html', {'menu': menu})
    else:
        return redirect(reverse('practice:login'))

