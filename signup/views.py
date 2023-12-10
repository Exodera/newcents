from django.shortcuts import render

def index(response):
    return render(response, 'signup/index.html',{})

def create_account(request):
    username = request.POST.get('username')
    print(username)
    password = request.POST.get('password')


# Create your views here.
