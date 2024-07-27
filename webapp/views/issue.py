from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from webapp.models.issue import Issue
from webapp.forms.issue import IssueForm
from webapp.models.project import Project


class IssueDetailView(DetailView):
    model = Issue
    template_name = 'issues/issue_detail.html'
    context_object_name = 'issue'


class IssueCreateView(LoginRequiredMixin, CreateView):
    model = Issue
    form_class = IssueForm
    template_name = 'issues/issue_form.html'

    def form_valid(self, form):
        project_pk = self.kwargs['project_pk']
        project = get_object_or_404(Project, pk=project_pk)
        issue = form.save(commit=False)
        issue.project = project
        issue.save()
        form.save_m2m()
        return redirect('project_detail', pk=project.pk)


    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.kwargs['project_pk']})


class IssueUpdateView(LoginRequiredMixin, UpdateView):
    model = Issue
    form_class = IssueForm
    template_name = 'issues/issue_form.html'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.project.pk})


class IssueDeleteView(LoginRequiredMixin, DeleteView):
    model = Issue
    template_name = 'issues/issue_confirm_delete.html'
    context_object_name = 'issue'

    def get_success_url(self):
        return reverse('project_list')

