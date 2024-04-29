from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "issues/index.html")
