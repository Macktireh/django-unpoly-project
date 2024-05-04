from django.contrib import admin
from django.db import models
from mdeditor.widgets import MDEditorWidget
from unfold.admin import ModelAdmin

from apps.issues.models import Issue, Tag


@admin.register(Issue)
class IssueAdmin(ModelAdmin):
    list_display = ("title", "created", "updated")
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget},
    }
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Tag)
class LabelAdmin(ModelAdmin):
    list_display = ("name", "color", "description")
    list_editable = ("color", "description")
