from django.urls import path
from .views import *

app_name = 'groups'

urlpatterns = [
    path('', ListGroup.as_view(template_name = 'group_list.html'), name='all'),
    path('new/', CreateGroup.as_view(template_name = 'group_form.html'), name='create'),
    path('posts/in/<slug:slug>', SingleGroup.as_view(template_name = 'group_detail.html'), name='single'),
    path('join/<slug:slug>', JoinGroup.as_view(), name='join'),
    path('leave/<slug:slug>', LeaveGroup.as_view(), name='leave'),
]