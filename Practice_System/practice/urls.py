from django.urls import path
from practice import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
]