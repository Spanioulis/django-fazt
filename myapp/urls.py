from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/<str:username>', views.hello, name='hello'),
    path('about/', views.about, name='about'),
    path('persons/', views.persons, name='persons'),
    path('tasks/', views.tasks, name='tasks'),
    path('create-task/', views.create_task, name='create-task'),
]