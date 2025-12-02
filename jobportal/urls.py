"""
URL configuration for jobportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from job.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name = 'index'),
    path('admin_login', admin_login ,name = 'admin_login'),
    path('user_login', user_login ,name = 'user_login'),
    path('recruiter_login', recruiter_login ,name = 'recruiter_login'),
    path('user_signup', user_signup ,name = 'user_signup'),
    path('user_home', user_home ,name = 'user_home'),
    path('recruiter_home', recruiter_home ,name = 'recruiter_home'),
    path('admin_home', admin_home ,name = 'admin_home'),
    path('recruiter_signup', recruiter_signup ,name = 'recruiter_signup'),
    path('view_user', view_user ,name = 'view_user'),
    path('delete_user/<int:pid>', delete_user ,name = 'delete_user'),
    path('change_status/<int:pid>', change_status ,name = 'change_status'),
    path('recruiter_pending', recruiter_pending ,name = 'recruiter_pending'),
    path('recruiter_accepted', recruiter_accepted ,name = 'recruiter_accepted'),
    path('recruiter_rejected', recruiter_rejected ,name = 'recruiter_rejected'),
    path('recruiter_all', recruiter_all ,name = 'recruiter_all'),
    path('delete_recruiter/<int:pid>', delete_recruiter ,name = 'delete_recruiter'),
    path('change_password_admin', change_password_admin ,name = 'change_password_admin'),
    path('change_password_user', change_password_user ,name = 'change_password_user'),
    path('change_password_recruiter', change_password_recruiter ,name = 'change_password_recruiter'),
    path('edit_jobdetail/<int:pid>', edit_jobdetail ,name = 'edit_jobdetail'),
    path('change_companylogo/<int:pid>', change_companylogo ,name = 'change_companylogo'),
    path('add_job', add_job ,name = 'add_job'),
    path('job_list', job_list ,name = 'job_list'),
    path('latest_jobs', latest_jobs, name='latest_jobs'),
    path('apply_for_job/<int:pid>', apply_for_job, name='apply_for_job'),
    path('my_applications', my_applications, name='my_applications'),
    path('recruiter_applications/<int:pid>', recruiter_applications, name='recruiter_applications'),
    path('update_application_status/<int:pid>', update_application_status, name='update_application_status'),
    path('Logout', Logout ,name = 'Logout'),
    
    # Password Reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]

from django.views.static import serve 
from django.urls import re_path

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),]
