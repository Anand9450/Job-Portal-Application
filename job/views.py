from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def index(request):
    return render(request, 'index.html')


def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username = u, password = p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {"error":error}
    return render(request, 'admin_login.html', d)


def user_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = StudentUser.objects.get(user=user)
                if user1.type == 'student':
                    login(request, user)
                    error='no'
                else:
                    error = 'yes'
            except:
                error = 'yes'
        else:
            error='yes'
    d = {'error' : error}
    return render(request, 'user_login.html', d)

def recruiter_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = Recruiter.objects.get(user=user)
                if user1.type == 'recruiter' and user1.status != 'pending':
                    login(request, user)
                    error = 'no'
                else:
                    error = 'not'
            except:
                error = 'yes'
        else:
            error = 'yes'
    d = {'error': error}
    return render(request, 'recruiter_login.html')

def recruiter_signup(request):
    error = ""
    if request.method == "POST":
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        gen = request.POST['gender']
        company = request.POST['company']
        try:
            user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
            Recruiter.objects.create(user=user, mobile=con, image=i, gender=gen, company = company, type="recruiter", status = "pending")
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request,'recruiter_signup.html')

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login.html')
    return render(request, 'user_home.html')


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login.html')
    return render(request, 'admin_home.html')


def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login.html')
    return render(request, 'recruiter_home.html')
def Logout(request):
    logout(request)
    return redirect('index')

def user_signup(request):
    error = ""
    if request.method == "POST":
        f = request.POST['fname']
        l = request.POST['lname']
        i = request.FILES['image']
        p = request.POST['pwd']
        e = request.POST['email']
        con = request.POST['contact']
        gen = request.POST['gender']
        try:
            user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
            StudentUser.objects.create(user = user, mobile = con, image =i, gender = gen, type="student")
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request,'user_signup.html', d)


def view_user(request):
    if not request.user.is_authenticated:
        return redirect('admin_login.html')
    data = StudentUser.objects.all()
    d = {'data': data}
    return render(request, 'view_user.html', d)


def delete_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login.html')
    student = StudentUser.objects.get(id = pid)
    student.delete()
    return redirect('view')


def recruiter_pending(request):
    if not request.user.is_authenticated:
        return redirect('admin_login.html')
    data = Recruiter.objects.filter(status = 'pending')
    d = {'data': data}
    return render(request, 'recruiter_pending.html', d)


def recruiter_accepted(request):
    if not request.user.is_authenticated:
        return redirect('admin_login.html')
    data = Recruiter.objects.filter(status = 'Accept')
    d = {'data': data}
    return render(request, 'recruiter_pending.html', d)



def recruiter_rejected(request):
    if not request.user.is_authenticated:
        return redirect('admin_login.html')
    data = Recruiter.objects.filter(status = 'Rejected')
    d = {'data': data}
    return render(request, 'recruiter_pending.html', d)


def change_status(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login.html')
    error = ""
    recruiter = Recruiter.objects.get(id = pid)
    if request.method == 'POST':
        s = request.post['status']
        recruiter.status = s
        try:
            recruiter.save()
            error = 'no'
        except:
            error = 'yes'
    d = {'data': recruiter, 'error': error}
    return render(request, 'change_status.html', d)