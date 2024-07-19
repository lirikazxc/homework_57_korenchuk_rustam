from django import forms

from webapp.forms.validations import val_sum_len, val_bad_words
from webapp.models.issue import Issue, Type, Status


class IssueForm(forms.ModelForm):
    summary = forms.CharField(validators=[val_sum_len])
    description = forms.CharField(validators=[val_bad_words])
    types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), required=True, widget=forms.CheckboxSelectMultiple)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True)

    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'types']
