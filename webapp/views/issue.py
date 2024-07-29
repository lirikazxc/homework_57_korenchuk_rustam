from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
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


class IssueCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = 'webapp.add_issue'
    model = Issue
    form_class = IssueForm
    template_name = 'issues/issue_form.html'

    def has_permission(self):
        project = get_object_or_404(Project, pk=self.kwargs['project_pk'])
        return super().has_permission() and self.request.user in project.users.all()

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


class IssueUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = 'webapp.change_issue'
    model = Issue
    form_class = IssueForm
    template_name = 'issues/issue_form.html'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.project.pk})

    def has_permission(self):
        self.object = self.get_object()
        project = self.object.project
        if not super().has_permission() or self.request.user not in project.users.all():
            raise PermissionDenied
        return True


class IssueDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = 'webapp.delete_issue'
    model = Issue
    template_name = 'issues/issue_confirm_delete.html'
    context_object_name = 'issue'

    def has_permission(self):
        self.object = self.get_object()
        project = self.object.project
        if not super().has_permission() or self.request.user not in project.users.all():
            raise PermissionDenied
        return True

    def get_success_url(self):
        return reverse('project_list')
