from django import forms
from .models import Issue, Type, Status


class IssueForm(forms.ModelForm):
    types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), required=True, widget=forms.CheckboxSelectMultiple)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True)

    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'types']
