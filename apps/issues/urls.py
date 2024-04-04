from django.urls import path

from apps.issues.views import HomeView

app_name = "issues"

urlpatterns = [
    path("", HomeView.as_view()),
]
