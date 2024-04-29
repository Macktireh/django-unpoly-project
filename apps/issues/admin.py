from django.contrib import admin
from unfold.admin import ModelAdmin

from apps.issues.models import Issue, Tag


@admin.register(Issue)
class IssueAdmin(ModelAdmin):
    list_display = ("title", "created", "updated")


@admin.register(Tag)
class LabelAdmin(ModelAdmin):
    list_display = ("name", "color", "description")
    list_editable = ("color", "description")
