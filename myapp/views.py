from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Person, Task

# Create your views here.

def index(request):
  return HttpResponse("<h1>Home Page!</h1>")

def hello(request, username):
  return HttpResponse("<h1>Hola %s!</h1>" % username)

def about(request):
  return HttpResponse("<h1>About</h1>")

def persons(request):
  persons = list(Person.objects.values())
  return JsonResponse(persons, safe=False)

def tasks(request, id):
  task = get_object_or_404(Task, id=id)
  return HttpResponse('task: %s' % task.title)