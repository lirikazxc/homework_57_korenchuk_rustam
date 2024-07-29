from django import forms
from django.contrib.auth.models import User
from webapp.models.project import Project


class ProjectUserForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Project
        fields = ['users']