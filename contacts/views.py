from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.http import JsonResponse

from taggit.models import Tag
from .models import Contact
from .forms import ContactCreateForm, ContactUpdateForm


class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    success_url = "/"


def success(request):
    return render(request, "contacts/success.html")


# A View to delete multiple contacts at once!
def delete(request):
    if request.method == "POST":
        try:
            ids_list = request.POST.getlist("ids_list[]")
            delete_objects = Contact.objects.filter(id__in=ids_list)
            delete_objects.delete()
            return JsonResponse({})
        except:
            return JsonResponse("error", status=404)


class ContactListView(LoginRequiredMixin, ListView):
    paginate_by = 5

    model = Contact
    # <app> / <model>_<viewtype>.html
    context_object_name = "contacts"

    def get_context_data(self, *args, **kwargs):
        context = super(ContactListView, self).get_context_data(*args, **kwargs)
        user = get_object_or_404(User, username=self.request.user.username)
        context["tags"] = set()
        for tag in Tag.objects.filter(contact__parent_user=user):
            context["tags"].update([tag])
        context["total"] = Contact.objects.filter(parent_user=self.request.user).count()
        return context

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user.username)
        return Contact.objects.filter(parent_user=user)


class ContactTagListView(ContactListView):
    def get_context_data(self, *args, **kwargs):
        context = super(ContactListView, self).get_context_data(*args, **kwargs)
        user = get_object_or_404(User, username=self.request.user.username)
        context["tags"] = set()
        for tag in Tag.objects.filter(contact__parent_user=user):
            context["tags"].update([tag])
        context["total"] = Contact.objects.filter(parent_user=self.request.user).count()
        return context

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user.username)
        if self.kwargs["tag"] == "all":
            return Contact.objects.filter(parent_user=user)
        else:
            return Contact.objects.filter(
                tags__name=self.kwargs["tag"], parent_user=user
            )


class ContactDetailView(LoginRequiredMixin, DetailView):
    # TODO implement safety of login required attribute if UID is stolen
    model = Contact


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    # TODO add request to merge with already existing contact during creation

    form_class = ContactCreateForm
    success_url = "/"

    def get_form_kwargs(self):
        kw = super(ContactCreateView, self).get_form_kwargs()
        kw["request"] = self.request
        return kw

    def form_valid(self, form):
        form.instance.parent_user = self.request.user
        return super().form_valid(form)


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact
    form_class = ContactUpdateForm

    # TODO implement sessions, hold data of contact being edited, and save in session
    # TODO add request to merge with already existing contact during updating contact
    def form_valid(self, form):
        return super().form_valid(form)
