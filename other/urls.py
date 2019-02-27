
from django.urls import path
from . import views
urlpatterns = [
    path ('',views.home, name='home'),
    path ('notice-list',views.notice_list, name='notice_list'),
    path ('notice-list/<slug>',views.notice_details, name ='notice_details')
]
