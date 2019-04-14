from django.urls import path
from practice.teacher import views

app_name = 'practice.teacher'
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('postmanage/', views.postmanage, name='postmanage'),
    path('browsejobs/', views.browsejobs, name='browsejobs'),
    path('studentmanage/', views.studentmanage, name='studentmanage'),
    path('browseweeklyreport/', views.browseweeklyreport, name='browseweeklyreport'),
    path('unread/', views.unread, name='unread'),
    path('readed/', views.readed, name='readed'),
]
