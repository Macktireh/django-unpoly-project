from random import choice

from colorfield.fields import ColorField
from django.db import models


def generate_hex_color() -> str:
    hex_chars = "0123456789ABCDEF"
    color = "#"
    for _ in range(6):
        color += choice(hex_chars)
    return color


class TimestampMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(TimestampMixin):
    name = models.CharField(max_length=64)
    color = ColorField(default=generate_hex_color)
    description = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        db_table = "tags"
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Issue(TimestampMixin):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, db_index=True)
    description = models.TextField(null=True, blank=True)
    labels = models.ManyToManyField(to=Tag, related_name="issues", db_table="issues_labels")

    class Meta:
        db_table = "issues"
        ordering = ["-created"]

    def __str__(self) -> str:
        return self.title
