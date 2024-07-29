from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from webapp.models.issue import Issue
from webapp.models.project import Project
from webapp.forms.project import ProjectUserForm


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return Project.objects.filter(name__icontains=query) | Project.objects.filter(description__icontains=query)
        return Project.objects.all()


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.filter(project=self.object)
        return context


class ProjectCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    permission_required = 'webapp.change_project'
    model = Project
    fields = ['start_date', 'end_date', 'name', 'description']
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        context = super().form_valid(form)
        self.object.users.add(self.request.user)
        return context


class ProjectUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    permission_required = 'webapp.change_project'
    model = Project
    fields = ['start_date', 'end_date', 'name', 'description']
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project_list')

    def has_permission(self):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        return super().has_permission() and self.request.user in project.users.all()


class ProjectDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
    permission_required = 'webapp.change_project'
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')

    def has_permission(self):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        return super().has_permission() and self.request.user in project.users.all()


class ProjectUserView(PermissionRequiredMixin, UpdateView):
    permission_required = 'webapp.change_user_to_project'
    model = Project
    form_class = ProjectUserForm
    template_name = 'projects/project_users_form.html'

    def has_permission(self):
        project = get_object_or_404(Project, pk=self.kwargs['pk'])
        return super().has_permission() and self.request.user in project.users.all()

    def get_success_url(self):
        return reverse_lazy('project_detail', kwargs={'pk': self.object.pk})
