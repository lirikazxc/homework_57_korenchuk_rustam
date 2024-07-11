from django import forms
from .models import Issue, Type, Status


class IssueForm(forms.ModelForm):
    type = forms.ModelChoiceField(queryset=Type.objects.all(), required=True)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True)

    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'type']
