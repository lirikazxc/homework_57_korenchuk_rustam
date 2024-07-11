from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView

from .models import Issue
from .forms import IssueForm


class IssueListView(TemplateView):
    template_name = 'issue_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
        return context


class IssueDetailView(TemplateView):
    template_name = 'issue_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue = get_object_or_404(Issue, pk=self.kwargs['pk'])
        context['issue'] = issue
        return context


class IssueCreateView(View):
    def get(self, request):
        form = IssueForm()
        return render(request, 'issue_form.html', {'form': form})

    def post(self, request):
        form = IssueForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('issue_list')
        return render(request, 'issue_form.html', {'form': form})


class IssueUpdateView(View):
    def get(self, request, pk):
        issue = get_object_or_404(Issue, pk=pk)
        form = IssueForm(instance=issue)
        return render(request, 'issue_form.html', {'form': form})

    def post(self, request, pk):
        issue = get_object_or_404(Issue, pk=pk)
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('issue_list')
        return render(request, 'issue_form.html', {'form': form})


class IssueDeleteView(View):
    def get(self, request, pk):
        issue = get_object_or_404(Issue, pk=pk)
        return render(request, 'issue_confirm_delete.html', {'issue': issue})

    def post(self, request, pk):
        issue = get_object_or_404(Issue, pk=pk)
        issue.delete()
        return redirect('issue_list')
