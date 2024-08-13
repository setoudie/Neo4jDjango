from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('create/', views.create_prompt, name='create_prompt'),
    path('update/<str:prompt_id>/', views.update_prompt, name='update_prompt'),
    path('delete/<str:prompt_id>/', views.delete_prompt, name='delete_prompt'),
    path('dashboard/', views.show_all_prompt, name='show_all_prompt')
]
