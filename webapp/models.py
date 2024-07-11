from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"Статус: {self.name}"


class Type(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Тип: {self.name}"


class Issue(models.Model):
    summary = models.CharField(max_length=150, verbose_name="Заголовок")
    description = models.TextField(blank=True, null=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    types = models.ManyToManyField(Type)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Заголовок: {self.summary}"
