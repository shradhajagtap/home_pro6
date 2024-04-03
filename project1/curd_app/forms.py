from django import forms
from .models import CJC


class CJCForm(forms.ModelForm):
    class Meta:
        model = CJC
        fields = "__all__"

        widgets = {
            "stu_first_name": forms.TextInput(attrs={"class": "forms-control"}),
            "stu_last_name": forms.TextInput(attrs={"class": "forms-control"}),
            "stu_qualification": forms.TextInput(attrs={"class": "forms-control"}),
            "course": forms.RadioSelect(attrs={"class": "forms-control"}),
            "stu_address": forms.TextInput(attrs={"class": "forms-control"})
        }
