from django.urls import path

from . import views

urlpatterns = [
    path("", views.ContactListView.as_view(), name="home"),
    path(
        "contact/tag/<str:tag>/",
        views.ContactTagListView.as_view(),
        name="contact-tags",
    ),
    path("contact/new-contact/", views.ContactCreateView.as_view(), name="create"),
    path(
        "contact/<str:pk>/", views.ContactDetailView.as_view(), name="contact-details"
    ),
    path("success/", views.success, name="success"),
    path("delete-multiple/", views.delete, name="delete-multiple"),
    path(
        "contact/<str:pk>/delete/",
        views.ContactDeleteView.as_view(),
        name="contact-delete",
    ),
    path(
        "contact/<str:pk>/update/",
        views.ContactUpdateView.as_view(),
        name="contact-update",
    ),
]
