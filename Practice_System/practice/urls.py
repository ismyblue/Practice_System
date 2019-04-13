from django.urls import path,include
from practice import views

app_name = 'practice'
urlpatterns = [
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('dologin/', views.dologin, name='dologin'),
    path('index/', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
]