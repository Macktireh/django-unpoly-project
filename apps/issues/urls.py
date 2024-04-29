from django.urls import path

from apps.issues.views import IndexView

app_name = "issues"

urlpatterns = [
    path("", IndexView.as_view()),
]
