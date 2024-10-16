from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from .models import Person, Task

# Create your views here.

def index(request):
  title = 'Welcome to Django Fazt!!'
  return render(request, 'index.html', {
    "title": title
  })

def hello(request, username):
  return HttpResponse("<h1>Hola %s!</h1>" % username)

def about(request):
  username = 'Spanioulis'
  return render(request, 'about.html', {
    "username": username
  })

def persons(request):
  # persons = list(Person.objects.values())
  # return JsonResponse(persons, safe=False)
  persons = Person.objects.all( )

  return render(request, 'persons.html', {
    "persons": persons,
  })

def tasks(request):
  # task = get_object_or_404(Task, id=id)
  # return HttpResponse('task: %s' % task.title)
  tasks = Task.objects.all()
  return render(request, 'tasks.html', {
    'tasks': tasks,
  })