from django.urls import path
from . import views

urlpatterns =[
        path('', views.index),
        path('<str:app_link>/', views.appmain )
]
