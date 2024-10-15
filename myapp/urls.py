from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('hello/<str:username>', views.hello),
    path('about/', views.about),
    path('persons/', views.persons),
    path('tasks/<int:id>', views.tasks)
]