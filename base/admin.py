from django.contrib import admin
from .models import Task
from django.contrib.auth.models import Group


admin.site.site_header = 'To-Do-List Admin Dashboard'
admin.site.register(Task)
admin.site.unregister(Group)