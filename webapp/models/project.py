from django.db import models


class Project(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
