from django.urls import path
from practice.student import views

app_name = 'practice.student'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('browsejobs/', views.browsejobs, name='browsejobs'),
    path('showjob/<int:job_id>/', views.showjob, name='showjob'),
    path('information/<int:ent_id>/', views.information, name='information'),
    path('sendresume/<int:job_id>/', views.sendresume, name='sendresume'),
    path('applied/', views.applied, name='applied'),  #查看已投递简历
    path('newreport/', views.newreport, name='newreport'),      # 新建周记菜单
    path('savereport/', views.savereport, name='newreport'),      # 保存周记
    path('editreport/<int:weekRecord_id>/', views.editreport, name='editreport'),      # 修改周记
    path('updatereport/<int:weekRecord_id>/', views.updatereport, name='updatereport'),      # update周记
    path('deletereport/<int:weekRecord_id>/', views.deletereport, name='deletereport'),  # 删除周记
    path('showreport/<int:weekRecord_id>/', views.showreport, name='showreport'),  # 展示report
    path('reporthistory/', views.reporthistory, name='reporthistory'),  # 已写周记菜单
]
