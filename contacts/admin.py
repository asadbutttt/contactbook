from django.contrib import admin
from .models import Contact
from django.http import HttpResponseServerError

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('f_name','l_name',  'parent_user', 'phone', 'get_tags')
    search_fields = ['parent_user']

    def get_tags(self, obj):
        return ", ".join(o for o in obj.tags.names())