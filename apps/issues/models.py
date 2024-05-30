from random import choice
from typing import override

from colorfield.fields import ColorField
from django.core.validators import MinLengthValidator
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from mdeditor.fields import MDTextField


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
    title = models.CharField(max_length=255, validators=[MinLengthValidator(6)])
    slug = models.SlugField(unique=True, max_length=255, db_index=True)
    content = MDTextField(null=True, blank=True, validators=[MinLengthValidator(10)])
    tags = models.ManyToManyField(to=Tag, related_name="issues", db_table="issues_tags", blank=True)

    @override
    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def get_absolute_url(self) -> str:
        return reverse("issues:detail", kwargs={"slug": self.slug})

    class Meta:
        db_table = "issues"
        ordering = ["-created"]

    def __str__(self) -> str:
        return self.title
