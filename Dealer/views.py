from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Vehiculos
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import taskform
from django.utils import timezone
from django.contrib.auth.decorators import login_required



# Create your views here.

def home(request): 
    return render(request, 'home.html')

#log in
def singup(request): 
    if request.method == 'GET': 
        return render(request, 'singup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']: 
            try : 
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('task')
            except: IntegrityError
        return render(request, 'singup.html', {
            'form': UserCreationForm, 'error': 'Passwords do not match or user exist'
            })
@login_required
def task(request): 
    task = Vehiculos.objects.filter(user= request.user, sold__isnull = True)
    return render(request, 'task.html', {
        'form': task
    })
@login_required
def signout(request): 
    logout(request)
    return redirect('home')

def signin(request): 
    if request.method == "GET": 
        return render(request, 'singin.html', {
            'form': AuthenticationForm
        })
    else: 
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None: 
            return render(request, 'singin.html', {
                'form': AuthenticationForm, 'error': "User or password incorrect"
            })
        else: 
            login(request, user)
            return redirect('task')
@login_required
def create_vehicle(request): 
    if request.method == 'GET': 
        return render(request, 'create_vehicle.html', {
            'form': taskform
        })
    else: 
        try: 
            form = taskform(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('task')
        except:
            return render(request, 'create_vehicle.html', {
                'form': taskform, 'error': "Data invalid"
            })
@login_required
def vehicle_details(request, vehicle_id): 
    if request.method == 'GET':
        vehicle = get_object_or_404(Vehiculos, pk= vehicle_id, user = request.user)
        form = taskform(instance=vehicle)
        return render(request, 'vehicles_details.html', {
            'vehicle': vehicle, 'form': form
        })
    else: 
        try: 
            vehicle = get_object_or_404(Vehiculos, pk =vehicle_id, user = request.user)
            form = taskform(request.POST, instance=vehicle)
            form.save()
            return redirect('task')
        except: 
            return render(request, 'vehicles_details.html', {
                'form': form , 'error': "Error updating", 'vehicle': vehicle
            })
@login_required
def sell(request, vehicle_id):
    vehicle = get_object_or_404(Vehiculos, pk=vehicle_id, user = request.user)
    if request.method == 'POST': 
        vehicle.sold = timezone.now()
        vehicle.save()
        return redirect('task')
@login_required
def delete(request, vehicle_id): 
    vehicle = get_object_or_404(Vehiculos, pk = vehicle_id, user = request.user)
    if request.method == 'POST': 
        vehicle.delete()
        return redirect('task')
@login_required
def vehicle_sold(request): 
    vehicle = Vehiculos.objects.filter(user = request.user, sold__isnull=False).order_by('-sold')
    return render(request, 'task.html', {
        'form': vehicle
    })