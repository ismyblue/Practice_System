from django.urls import path
from practice.enterprise import views

app_name = 'practice.enterprise'
urlpatterns = [
    path('', views.index, name='index'),
]
