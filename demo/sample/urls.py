from django.contrib import admin
from django.urls import path
from sample.views import index,demo,service,about,base
from sample.views import*


urlpatterns = [
    
    path('index',index,name='index'),
    path('demo',demo,name='skill'),
    path('services',service,name='home'),
     path('about',about,name='about'),
     path('',base,name='base'),
   
    path('send_message/', send_message, name='send_message'),
    path('inbox/', inbox, name='inbox'),
    path('delete_message/<int:message_id>/', delete_message, name='delete_message'),
    path('send_file/', send_file, name='send_file'),
    path('files_received/', files_received, name='files_received'),
]
