from django.shortcuts import render
from allapps.models import App

def base(request):
    app_list = App.objects.all()
    context ={
        "app_list" : app_list
    }
    return render(request, 'insurcents/homepage.html', context)

