from django import forms
from .models import Contact


class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "image",
            "f_name",
            "l_name",
            "mobile_phone",
            "work_phone",
            "home_phone",
            "tags",
            "email",
            "dob",
            "address",
            "notes",
        ]


class ContactUpdateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "image",
            "f_name",
            "l_name",
            "mobile_phone",
            "work_phone",
            "home_phone",
            "tags",
            "email",
            "dob",
            "address",
            "notes",
        ]
