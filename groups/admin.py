from django.contrib import admin
from .models import *

class GroupMemberInline(admin.TabularInline):
    model = GroupMember

admin.site.register(Group)
