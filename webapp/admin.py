from django.contrib import admin
from webapp.models.issue import Status, Type, Issue
from webapp.models.project import Project

admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Issue)
admin.site.register(Project)