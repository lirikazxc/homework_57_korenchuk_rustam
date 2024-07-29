from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from webapp.models.issue import Issue
from webapp.models.project import Project


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


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['start_date', 'end_date', 'name', 'description']
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        context = super().form_valid(form)
        self.object.users.add(self.request.user)
        return context


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ['start_date', 'end_date', 'name', 'description']
    template_name = 'projects/project_form.html'
    success_url = reverse_lazy('project_list')


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')


