from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import date

# Create your views here.


def index(request):
    jobs = Job.objects.all().order_by('-creation_date')
    user = request.user
    applied_job_ids = []
    if user.is_authenticated:
        try:
            student = StudentUser.objects.get(user=user)
            applied_job_ids = list(Apply.objects.filter(student=student).values_list('job_id', flat=True))
        except:
            pass
    d = {'jobs': jobs, 'applied_job_ids': applied_job_ids}
    return render(request, 'index.html', d)


def admin_login(request):
    if request.user.is_authenticated:
        return redirect('admin_home')
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
    if request.user.is_authenticated:
        return redirect('user_home')
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
    if request.user.is_authenticated:
        return redirect('recruiter_home')
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
            if User.objects.filter(username=e).exists():
                error = "yes"
            else:
                user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
                Recruiter.objects.create(user=user, mobile=con, image=i, gender=gen, company = company, type="recruiter", status = "pending")
                error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request,'recruiter_signup.html', d)

def user_home(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    student = StudentUser.objects.get(user=user)
    error = ""
    if request.method == "POST":
        f = request.POST['fname']
        l = request.POST['lname']
        con = request.POST['contact']
        gen = request.POST['gender']
        exp = request.POST['experience']
        skills = request.POST['skills']
        social = request.POST['social']

        student.user.first_name = f
        student.user.last_name = l
        student.mobile = con
        student.gender = gen
        student.experience = exp
        student.skills = skills
        student.social_link = social

        try:
            student.save()
            student.user.save()
            error = "no"
        except:
            error = "yes"

        try:
            i = request.FILES['image']
            student.image = i
            student.save()
            error = "no"
        except:
            pass
        
        try:
            r = request.FILES['resume']
            student.resume = r
            student.save()
            error = "no"
        except:
            pass

    d = {'student': student, 'error': error}
    return render(request, 'user_home.html',d)

def apply_for_job(request, pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    student = StudentUser.objects.get(user=user)
    job = Job.objects.get(id=pid)
    date1 = date.today()
    error = ""
    
    try:
        application = Apply.objects.get(student=student, job=job)
    except Apply.DoesNotExist:
        application = None

    if request.method == 'POST':
        cl = request.POST['cover_letter']
        try:
            if application:
                application.cover_letter = cl
                application.resume = student.resume
                application.apply_date = date1
                application.save()
                error = "done"
            else:
                Apply.objects.create(job=job, student=student, resume=student.resume, apply_date=date1, cover_letter=cl, status="Pending")
                error = "done"
        except:
            error = "error"
        d = {'error': error}
        return render(request, 'apply_success.html', d)
        
    d = {'job': job, 'student': student, 'application': application}
    return render(request, 'apply_form.html', d)

def my_applications(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = request.user
    student = StudentUser.objects.get(user=user)
    applications = Apply.objects.filter(student=student).order_by('-apply_date')
    d = {'applications': applications}
    return render(request, 'my_applications.html', d)


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')


def recruiter_home(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    recruiter = Recruiter.objects.get(user = user)
    error = ""
    if request.method == "POST":
        f = request.POST['fname']
        l = request.POST['lname']
        con = request.POST['contact']
        gen = request.POST['gender']

        recruiter.user.first_name= f
        recruiter.user.last_name = l
        recruiter.mobile = con
        recruiter.gender = gen

        try:
            recruiter.save()
            recruiter.user.save()
            error = "no"
        except:
            error = "yes"


        try:
            i = request.FILES['image']
            recruiter.image = i
            recruiter.save()
            error = "no"
        except:
            pass

    d = {'recruiter':recruiter, 'error': error}
    return render(request, 'recruiter_home.html',d)

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
            if User.objects.filter(username=e).exists():
                error = "yes"
            else:
                user = User.objects.create_user(first_name=f, last_name=l, username=e, password=p)
                StudentUser.objects.create(user = user, mobile = con, image =i, gender = gen, type="student")
                error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request,'user_signup.html', d)


def view_user(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = StudentUser.objects.all()
    d = {'data': data}
    return render(request, 'view_user.html', d)


def delete_user(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    student = User.objects.get(id = pid)
    student.delete()
    return redirect('view_user')


def delete_recruiter(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    recruiter = User.objects.get(id = pid)
    recruiter.delete()
    return redirect('recruiter_all')


def recruiter_pending(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status = 'pending')
    d = {'data': data}
    return render(request, 'recruiter_pending.html', d)


def recruiter_accepted(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status = 'Accept')
    d = {'data': data}
    return render(request, 'recruiter_pending.html', d)



def recruiter_rejected(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.filter(status = 'Reject')
    d = {'data': data}
    return render(request, 'recruiter_rejected.html', d)

def recruiter_all(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    data = Recruiter.objects.all()
    d = {'data': data}
    return render(request, 'recruiter_all.html', d)


def change_status(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    recruiter = Recruiter.objects.get(id = pid)
    if request.method == 'POST':
        s = request.POST['status']
        recruiter.status = s
        try:
            recruiter.save()
            error = 'no'
        except:
            error = 'yes'
    d = {'recruiter': recruiter, 'error': error}
    return render(request, 'change_status.html', d)


def change_password_admin(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    if request.method == 'POST':
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id = request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = 'no'
            else:
                error = 'not'
        except:
            error = 'yes'
    d = {'error': error}
    return render(request, 'change_password_admin.html',d)


def change_password_user(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error = ""
    if request.method == 'POST':
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id = request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = 'no'
            else:
                error = 'not'
        except:
            error = 'yes'
    d = {'error': error}
    return render(request, 'change_password_user.html',d)


def change_password_recruiter(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    if request.method == 'POST':
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id = request.user.id)
            if u.check_password(c):
                u.set_password(n)
                u.save()
                error = 'no'
            else:
                error = 'not'
        except:
            error = 'yes'
    d = {'error': error}
    return render(request, 'change_password_recruiter.html',d)


def add_job(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    if request.method == "POST":
        jt = request.POST['jobtitle']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        sal = request.POST['salary']
        l = request.FILES['logo']
        exp = request.POST['experience']
        loc = request.POST['location']
        skills = request.POST['skills']
        des = request.POST['description']
        user = request.user
        recruiter = Recruiter.objects.get(user = user)

        try:
            Job.objects.create(recruiter=recruiter, start_date = sd, end_date = ed, title = jt, salary = sal, image =l, description= des, experience = exp, location= loc, skills =skills, creation_date=date.today())
            error = "no"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'add_job.html', d)


def edit_jobdetail(request, pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    error = ""
    job = Job.objects.get(id=pid)
    if request.method == "POST":
        jt = request.POST['jobtitle']
        sd = request.POST['startdate']
        ed = request.POST['enddate']
        sal = request.POST['salary']
        l = request.FILES['logo']
        exp = request.POST['experience']
        loc = request.POST['location']
        skills = request.POST['skills']
        des = request.POST['description']
        user = request.user
        recruiter = Recruiter.objects.get(user = user)

        job.title = jt
        job.salary = sal
        job.experience = exp
        job.location = loc
        job.description = des
        job.skills = skills

        try:
            job.save()
            error = "no"
        except:
            error = "yes"


        if sd:
            try:
                job.start_date = sd
                job.save()
            except:
                pass
        else:
            pass


        if ed:
            try:
                job.end_date = ed
                job.save()
            except:
                pass
        else:
            pass
    d = {'job': job, 'error': error}
    return render(request, 'edit_jobdetail.html', d)


def change_companylogo(request, pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')

    error = ""
    job = Job.objects.get(id=pid)
    if request.method == "POST":
        cl = request.FILES['logo']

        job.image = cl

        try:
            job.save()
            error = "no"
        except:
            error = "yes"


    d = {'job': job, 'error': error}
    return render(request, 'change_companylogo.html', d)

def job_list(request):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    user = request.user
    recruiter = Recruiter.objects.get(user=user)
    jobs = Job.objects.filter(recruiter=recruiter)
    d = {'jobs': jobs}
    return render(request, 'job_list.html', d)

def latest_jobs(request):
    jobs = Job.objects.all().order_by('-creation_date')
    user = request.user
    applied_job_ids = []
    if user.is_authenticated:
        try:
            student = StudentUser.objects.get(user=user)
            applied_job_ids = list(Apply.objects.filter(student=student).values_list('job_id', flat=True))
        except:
            pass
    d = {'jobs': jobs, 'applied_job_ids': applied_job_ids}
    return render(request, 'latest_jobs.html', d)

def recruiter_applications(request, pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    job = Job.objects.get(id=pid)
    applications = Apply.objects.filter(job=job).order_by('-apply_date')
    d = {'applications': applications, 'job': job}
    return render(request, 'recruiter_applications.html', d)

def update_application_status(request, pid):
    if not request.user.is_authenticated:
        return redirect('recruiter_login')
    if request.method == 'POST':
        status = request.POST['status']
        application = Apply.objects.get(id=pid)
        application.status = status
        application.save()
        return redirect('recruiter_applications', pid=application.job.id)
    return redirect('recruiter_home')