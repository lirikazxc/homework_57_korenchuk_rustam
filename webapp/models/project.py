from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    users = models.ManyToManyField(User, related_name='projects')

    class Meta:
        permissions = [
            ("change_user_to_project", "Can add or delete user to project"),
        ]

    def __str__(self):
        return self.name
