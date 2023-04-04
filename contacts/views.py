from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

from taggit.models import Tag
from .models import Contact
from .forms import ContactCreateForm, ContactUpdateForm

# Create your views here.

class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = Contact
    success_url ='/'

def success(request):
    return render(request, 'contacts/success.html')

class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    # <app> / <model>_<viewtype>.html
    context_object_name = 'contacts'

    def get_context_data(self,*args, **kwargs):
        context = super(ContactListView, self).get_context_data(*args,**kwargs)
        user = get_object_or_404(User, username=self.request.user.username)
        context['tags'] = set()
        for tag in Tag.objects.filter(contact__parent_user=user):
            context['tags'].update([tag])
        return context

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user.username)
        return Contact.objects.filter(parent_user=user)

class ContactTagListView(ContactListView):

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user.username)
        if self.kwargs['tag'] == "all":
            return Contact.objects.filter(parent_user=user)
        else:
            return Contact.objects.filter(tags__name=self.kwargs['tag'], parent_user=user)


class ContactDetailView(LoginRequiredMixin, DetailView):
    model = Contact

class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    form_class = ContactCreateForm
    success_url = "/"

    def form_valid(self, form):
        form.instance.parent_user = self.request.user
        return super().form_valid(form)
    
class ContactUpdateView(LoginRequiredMixin, UpdateView):
    model = Contact
    form_class = ContactUpdateForm

    def form_valid(self, form):
        return super().form_valid(form)