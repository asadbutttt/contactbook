from django import forms
from .models import Contact

class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['f_name', 'l_name', 'phone', 'image', 'tags']

class ContactUpdateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['f_name', 'l_name', 'phone', 'image', 'tags']