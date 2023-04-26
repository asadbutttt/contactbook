from django import forms
from django.shortcuts import get_object_or_404
from .models import Contact
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.exceptions import ValidationError


class ContactCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        self.user = self.request.user
        super(ContactCreateForm, self).__init__(*args, **kwargs)

    def clean_f_name(self):
        data = self.cleaned_data["f_name"].capitalize()
        return data

    def clean_l_name(self):
        data = self.cleaned_data["l_name"].capitalize()
        return data

    def clean_mobile_phone(self):
        mobile = self.cleaned_data["mobile_phone"]
        mobile_phone_query = Q(mobile_phone__exact=mobile)
        home_phone_query = Q(home_phone__exact=mobile)
        work_phone_query = Q(work_phone__exact=mobile)
        user_query = Q(parent_user=self.user)

        qs = Contact.objects.filter(
            user_query & (mobile_phone_query | work_phone_query | home_phone_query)
        ).count()
        if qs > 0:
            raise ValidationError("The mobile phone number is already taken!")

        return mobile

    def clean_home_phone(self):
        home = self.cleaned_data["home_phone"]
        mobile_phone_query = Q(mobile_phone__exact=home)
        home_phone_query = Q(home_phone__exact=home)
        work_phone_query = Q(work_phone__exact=home)
        user_query = Q(parent_user=self.user)

        qs = Contact.objects.filter(
            user_query & (mobile_phone_query | work_phone_query | home_phone_query)
        ).count()
        if qs > 0:
            raise ValidationError("The home phone number is already taken!")

        return home

    def clean_work_phone(self):
        work = self.cleaned_data["work_phone"]
        mobile_phone_query = Q(mobile_phone__exact=work)
        home_phone_query = Q(home_phone__exact=work)
        work_phone_query = Q(work_phone__exact=work)
        user_query = Q(parent_user=self.user)

        qs = Contact.objects.filter(
            user_query & (mobile_phone_query | work_phone_query | home_phone_query)
        ).count()
        if qs > 0:
            raise ValidationError("The work phone number is already taken!")

        return work

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
