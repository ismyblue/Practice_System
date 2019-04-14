from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect,reverse
from practice import daoapp

# 访问控制中间件，所有的用户请求都要经过这个中间件处理之后在发给urls.py去处理，
# 此中间件判断用户是否有权限访问相应资源，例如，student只能访问/practice/student/下的资源
# teacher只能访问/practice/teacher/下的资源
class AccessMiddleware(MiddlewareMixin):

    # 处理用户请求
    def process_request(self, request):
        session = request.session
        if not request.path.startswith('/admin/') and not request.path.startswith('/media/') \
                and request.path not in ['/practice/login/', '/practice/', '/practice/logout/', '/practice/index/']:
            print(session.items())
            if not 'role_id' in session.keys():
                session['role_id'] = -1
            role_id = int(session['role_id'])
            #获取此角色可访问的媒体资源列表
            # resource = daoapp.getResource(role_id)
            # if request.path not in resource:
            #     return redirect(reverse('practice:index'))
            if role_id == 1:
                if not request.path.startswith('/practice/admin/'):
                    print(role_id, request.path)
                    return redirect(reverse('practice:index'))
            elif role_id == 2:
                if not request.path.startswith('/practice/teacher/'):
                    print(role_id, request.path)
                    return redirect(reverse('practice:index'))
            elif role_id == 3:
                if not request.path.startswith('/practice/enterprise/'):
                    print(role_id, request.path)
                    return redirect(reverse('practice:index'))
            elif role_id == 4:
                if not request.path.startswith('/practice/student/'):
                    print(role_id, request.path)
                    return redirect(reverse('practice:index'))


