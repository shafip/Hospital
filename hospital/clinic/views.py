from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def home(request):
    return render(request,'login/guest.html')

def adddoctors(request):
    doctor = {
        'doc': DoctorIn.objects.all()
    }

    return render(request,'home/doctors.html',doctor)

def department(request):
    dict={
        'data':Department.objects.all()
    }

    return render(request,'home/department.html',dict)


def bookingview(request):
    if request.method=='POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home/home.html')
    form = BookingForm()
    dict={
        'form':form
    }
    return render(request,'home/booking.html',dict)











from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'hi{username},your account was created successfully')
            return redirect('patient')
    else:
        form = UserCreationForm()
    return render(request, 'login/register.html', {'form': form})


@login_required(login_url='profile')
def profile(request):
    return render(request, 'home/home.html')


#document

def viewpatient(request):
    dict = {
        'data': Booking.objects.all()
    }

    return render(request, 'home/patientview.html', dict)

def delete(request,pk):
    mod=Booking.objects.get(Token_id=pk)
    form=BookingForm(instance=mod)
    mod.delete()
    return redirect('home')