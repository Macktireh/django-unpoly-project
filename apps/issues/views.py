from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from apps.issues.forms import IssueForm
from apps.issues.models import Issue


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        query = request.GET.get("q")
        issues = Issue.objects.filter(title__icontains=query) if query else Issue.objects.all()
        context = {"issues": issues}
        return render(request=request, template_name="issues/index.html", context=context)


class CreateIssueView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {"form": IssueForm(), "action": reverse("issues:create"), "viewname": "Create"}
        return render(request=request, template_name="issues/create.html", context=context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = IssueForm(data=request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(reverse("issues:index"))
        context = {"form": form, "action": reverse("issues:create"), "viewname": "Create"}
        return render(request=request, template_name="issues/create.html", context=context)


class DetailIssueView(View):
    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        issue = get_object_or_404(Issue, slug=slug)
        context = {"issue": issue}
        return render(request=request, template_name="issues/detail.html", context=context)


class UpdateIssueView(View):
    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        issue = get_object_or_404(Issue, slug=slug)
        context = {
            "form": IssueForm(instance=issue),
            "action": reverse("issues:update", kwargs={"slug": slug}),
            "viewname": "Update",
        }
        return render(request=request, template_name="issues/create.html", context=context)

    def post(self, request: HttpRequest, slug: str) -> HttpResponse:
        issue = Issue.objects.get(slug=slug)
        form = IssueForm(data=request.POST or None, instance=issue)
        if form.is_valid():
            form.save()
            return redirect(reverse("issues:index"))
        context = {"form": form, "action": reverse("issues:update", kwargs={"slug": slug}), "viewname": "Update"}
        return render(request=request, template_name="issues/create.html", context=context)


class DeleteIssueView(View):
    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        issue = get_object_or_404(Issue, slug=slug)
        issue.delete()
        return redirect(reverse("issues:index"))
