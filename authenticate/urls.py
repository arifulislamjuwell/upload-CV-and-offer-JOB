from django.urls import path
from . import views
urlpatterns = [
    path ('registration/'     ,views.registration, name='registration'),
    path ('login/'            ,views.login,        name= 'login'),
    path ('logout/'           ,views.logout,       name= 'logout'),
    path ('create-profile/'   ,views.create_profile, name= 'profile'),
    path ('profile/<int:pk>/'          ,views.show_profile,name='show_profile'),
    path ('edit-remove-cv-job',views.edit_remove_job_cv,name='edit_cv_job')
]
