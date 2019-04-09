from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'practice/index.html')

def login(request):
    return render(request, 'practice/login.html')

def dologin(request):
    print(request.META)
    print(request.session)
    return redirect(reverse('practice:index'))
    # return render(request, 'practice/index.html')

