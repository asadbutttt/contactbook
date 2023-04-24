from django import forms
from .models import Contact


class ContactCreateForm(forms.ModelForm):
    def clean_f_name(self):
        data = self.cleaned_data["f_name"].capitalize()
        return data

    def clean_l_name(self):
        data = self.cleaned_data["l_name"].capitalize()
        return data

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
            "link",
            "notes",
        ]

        widgets = {
            "f_name": forms.TextInput(attrs={"placeholder": "John"}),
            "l_name": forms.TextInput(attrs={"placeholder": "Doe"}),
            "mobile_phone": forms.NumberInput(attrs={"placeholder": "+9300123457"}),
            "work_phone": forms.NumberInput(attrs={"placeholder": "+9300123457"}),
            "home_phone": forms.NumberInput(attrs={"placeholder": "+9300123457"}),
            "tags": forms.TextInput(attrs={"placeholder": "friend, work, new"}),
            "email": forms.EmailInput(attrs={"placeholder": "john@doe.com"}),
            "dob": forms.DateInput(attrs={"placeholder": "Jan 10, 1990"}),
            "address": forms.TextInput(attrs={"placeholder": "San Francisco, USA"}),
            "link": forms.TextInput(
                attrs={"placeholder": "https://github.com/facebook"}
            ),
            "notes": forms.TextInput(attrs={"placeholder": "Any details go here..."}),
        }


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
