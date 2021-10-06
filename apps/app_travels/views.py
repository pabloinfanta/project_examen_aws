from django.shortcuts import render, redirect
from apps.app_users.models import User
from apps.app_travels.models import Travel
from django.contrib import messages

def index(request):
  if 'userid' in request.session: 
    user = User.objects.get(id = request.session['userid'])
    context={
      "user": user,
      "travels": Travel.objects.exclude(users__id= user.id),
      "my_travels": user.travels.all()
    }
    return render(request, "app_travels/index.html", context)
  else:
    messages.info(request, "No puedes acceder a esta sección si no has iniciado sesión")
    return render(request, 'app_users/index.html')

def form_create(request):
  if 'userid' in request.session: 
    context={
      "user": User.objects.get(id = request.session['userid'])
    }
    return render(request, "app_travels/form_create.html", context)
  else:
    messages.info(request, "No puedes acceder a esta sección si no has iniciado sesión")
    return render(request, 'app_users/index.html')

def create_travel(request):
  errors = Travel.objects.basic_validator(request.POST)
  if len(errors) > 0:
    for key, value in errors.items():
      messages.error(request, value)
    return redirect('/travels/add')
  else:  
    user = User.objects.get(id= request.session['userid'])
    travel = Travel.objects.create(destination = request.POST['destination'], desc = request.POST['desc'],
                                  start_date = request.POST['start_date'], end_date = request.POST['end_date'],
                                  owner_user= user)
    travel.users.add(user)
    return redirect('/travels')

def add_user(request, id):
  travel= Travel.objects.get(id = id)
  user = User.objects.get(id = request.session['userid'])
  travel.users.add(user)
  return redirect('/travels')

def show_travel(request, id):
  if 'userid' in request.session: 
    travel= Travel.objects.get(id = id)
    user = User.objects.get(id = request.session['userid'])
    context={
      "travel": travel,
      "user": user,
    }
    return render(request, 'app_travels/show_travel.html', context)
  else:
    messages.info(request, "No puedes acceder a esta sección si no has iniciado sesión")
    return render(request, 'app_users/index.html')
