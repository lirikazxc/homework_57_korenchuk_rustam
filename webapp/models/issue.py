from django.db import models

from webapp.models.status import Status
from webapp.models.type import Type


class Issue(models.Model):
    summary = models.CharField(max_length=150, verbose_name="Заголовок")
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    types = models.ManyToManyField(Type)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Заголовок: {self.summary}"
