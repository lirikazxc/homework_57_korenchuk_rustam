from django import forms
from django.core.exceptions import ValidationError
from .models import Issue, Type, Status


def val_sum_len(value):
    if len(value) < 3:
        raise ValidationError('Описание должно быть длинее 3х символов')


def val_bad_words(value):
    bad_words = ['дурак', "stupid"]
    for word in bad_words:
        if word in value:
            raise ValidationError('Описание не должно содержать плохих слов!')

class IssueForm(forms.ModelForm):
    summary = forms.CharField(validators=[val_sum_len])
    description = forms.CharField(validators=[val_bad_words])
    types = forms.ModelMultipleChoiceField(queryset=Type.objects.all(), required=True, widget=forms.CheckboxSelectMultiple)
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=True)

    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'types']
