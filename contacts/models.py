import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField

from PIL import Image
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase


class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")
    f_name = models.CharField(_("First name"), max_length=255)
    l_name = models.CharField(_("Last name"), max_length=255)

    mobile_phone = PhoneNumberField(_("Mobile Phone"), blank=True, null=True)
    work_phone = PhoneNumberField(_("Work Phone"), blank=True, null=True)
    home_phone = PhoneNumberField(_("Home Phone"), blank=True, null=True)
    email = models.EmailField(_("Email address"), max_length=254, blank=True, null=True)
    address = models.CharField(_("Address"), max_length=255, blank=True, null=True)
    dob = models.DateField(_("Date of birth"), blank=True, null=True)
    notes = models.TextField(_("Notes"), max_length=500, blank=True, null=True)
    tags = TaggableManager(through=UUIDTaggedItem)

    # TODO add github link
    # BUG landline number cannot be added

    def __str__(self) -> str:
        return f"{self.f_name} Contact"

    def get_absolute_url(self):
        return reverse("contact-details", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        print(f"Current image path is: {self.image.path}")

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
