from django.urls import path

from apps.issues.views import CreateIssueView, DeleteIssueView, DetailIssueView, IndexView, UpdateIssueView

app_name = "issues"

urlpatterns = [
    path(route="", view=IndexView.as_view(), name="index"),
    path(route="issues/create", view=CreateIssueView.as_view(), name="create"),
    path(route="issues/<slug:slug>/", view=DetailIssueView.as_view(), name="detail"),
    path(route="issues/<slug:slug>/update", view=UpdateIssueView.as_view(), name="update"),
    path(route="issues/<slug:slug>/delete", view=DeleteIssueView.as_view(), name="delete"),
]
