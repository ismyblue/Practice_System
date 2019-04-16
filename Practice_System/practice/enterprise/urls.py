from django.urls import path
from practice.enterprise import views

app_name = 'practice.enterprise'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('postjobs/', views.postjobs, name='postjobs'),
    path('addjob/', views.addjob, name='addjob'),
    path('showjob/<int:job_id>/', views.showjob, name='showjob'),
    path('updatejob/<int:job_id>/', views.updatejob, name='updatejob'),
    path('deletejob/<int:job_id>/', views.deletejob, name='deletejob'),
    path('received/', views.received, name='received'),
    path('information/<int:stu_id>/', views.information, name='information'),
    path('select/<int:job_id>/<int:stu_id>/', views.select, name='select'),
    path('deletechoice/<int:job_id>/<int:stu_id>/', views.deletechoice, name='deletechoice'),
    path('selected/', views.selected, name='selected'),
    path('internmanage/', views.internmanage, name='internmanage'),
    path('mark/<int:stu_id>/<int:score>/', views.mark, name='mark'), # 为学生打分
]
