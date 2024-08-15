from django.urls import path
from . import views

urlpatterns =[
    path('login', views.login, name='login'),
    path('test', views.test, name='test'),
    path('create', views.create_user, name='create_user')
]
