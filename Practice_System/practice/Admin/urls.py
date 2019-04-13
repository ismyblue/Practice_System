from django.urls import path
from practice.Admin import views

urlpatterns = [
    path('', views.login, name='login'),
]
