from django.urls import path
from practice.teacher import views

app_name = 'practice.teacher'
urlpatterns = [
    path('', views.index, name='index'),
]
