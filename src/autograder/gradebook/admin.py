from django.contrib import admin
from .models import Assignment, Project, Test, Submit


admin.site.register(Assignment)
admin.site.register(Project)
admin.site.register(Test)
admin.site.register(Submit)