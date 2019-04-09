from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'practice/index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    return render(request, 'practice/login.html')
    # return HttpResponse('hello world')

