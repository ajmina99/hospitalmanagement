from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages

from app1.models import Doctor

from .forms import doctorform, appointmentform
from .models import Patient


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request,'about.html')

def department(request):
    return render(request,'department.html')


def vdoctor(request):
    d=Doctor.objects.all()
    return render(request,'view_doctor.html',{'doctor':d})

def adoctor(request):
    if (request.method == "POST"):  # after form submission
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        p = request.POST['p']
        s = request.POST.get('s')
        y = request.POST['y']
        i = request.FILES['i']  # uploaded files


        a = Doctor.objects.create(first_name=f,last_name=l,email=e,phone_number=p,specialization=s,experience_years=y,image=i)
        a.save()
        return vdoctor(request)
    return render(request,'add_doctor.html')

def contact(request):
    return render(request,'contact.html')

def register(request):
    if (request.method == "POST"):
        user = request.POST['user']
        p = request.POST['p']
        cp = request.POST['cp']
        fn = request.POST['f']
        ln = request.POST['l']
        e = request.POST['e']

        if (cp == p):
            user = User.objects.create_user(username=user,password=p, first_name=fn, last_name=ln, email=e)
            user.save()
            return redirect('login')
    return render(request,'register.html')

def user_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")
    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def delete(request,i):
    d=Doctor.objects.get(id=i)
    d.delete()
    return vdoctor(request)

@login_required
def edit(request, i):
    d = Doctor.objects.get(id=i)
    if (request.method == "POST"):

        form = doctorform(request.POST, request.FILES,
                        instance=d)

        if (form.is_valid()):
            form.save()
            return vdoctor(request)

    form = doctorform(instance=d)
    return render(request, 'edit_dr.html',{'form':form})

@login_required
def search_doctor(request):
        b = None
        query = ""
        if (request.method == "POST"):
            query = request.POST['q']
            if query:
                d = Doctor.objects.filter(Q(first_name__icontains=query) | Q(
                    specialization__icontains=query))

        return render(request, 'search_dr.html', {'doctor': d, 'query': query})

@login_required
def addpatient(request):
    if (request.method == "POST"):
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']
        p = request.POST['p']
        a = request.POST['a']
        dob = request.POST['dob']
        g = request.POST['g']
        mh = request.POST['mh']


        p = Patient.objects.create(first_name=f,last_name=l,email=e,phone_number=p,address=a,date_of_birth =dob,gender=g,medical_history=mh)
        p.save()
        return redirect('view_patient')
    return render(request,'add_patient.html')

@login_required
def viewpatient(request):
    p = Patient.objects.all()
    return render(request, 'view_patient.html', {'patient': p})

@login_required
def delete_pat(request,i):
    p=Patient.objects.get(id=i)
    p.delete()
    return viewpatient(request)

@login_required
def book_appointment(request):
    if (request.method=='POST'):
        form = appointmentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_success')  # Redirect to a success page or appointments list
    else:
        form = appointmentform()

    return render(request,'appointment.html',{'form':form})

@login_required
def appointment_success(request):
    return render(request,'appointment_success.html')

