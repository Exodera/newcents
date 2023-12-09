from django.shortcuts import render
from django.http import HttpResponse
from .models import App

def index(response):
    return render(response,"index.html", {} )

def appmain(response, app_link):
    app = App.objects.get(name=app_link)
    context ={
        "app":app
    }
    return render(response,"apps/appmain.html", context)
# Create your views here.
