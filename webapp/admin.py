from django.contrib import admin
from webapp.models.issue import Status, Type, Issue


admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Issue)