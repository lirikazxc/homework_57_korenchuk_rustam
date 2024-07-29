from django.urls import path
from webapp.views.project import ProjectListView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, \
    ProjectDetailView, ProjectUserView
from webapp.views.issue import IssueDetailView, IssueUpdateView, IssueDeleteView, IssueCreateView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project_list'),
    path('project/create/', ProjectCreateView.as_view(), name='project_create'),
    path('project/update/<int:pk>/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('project/delete/<int:pk>/', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/<int:project_pk>/issue/create/', IssueCreateView.as_view(), name='issue_create'),
    path('issue/<int:pk>/', IssueDetailView.as_view(), name='issue_detail'),
    path('issue/update/<int:pk>/', IssueUpdateView.as_view(), name='issue_update'),
    path('issue/delete/<int:pk>/', IssueDeleteView.as_view(), name='issue_delete'),
    path('projects/<int:pk>/update_users/', ProjectUserView.as_view(), name='project_update_users'),
]
