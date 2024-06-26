from django.forms import ModelForm, TextInput

from apps.issues.models import Issue


class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ["title", "content"]
        widgets = {
            "title": TextInput(
                attrs={
                    "class": "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"  # noqa: E501
                }
            )
        }
