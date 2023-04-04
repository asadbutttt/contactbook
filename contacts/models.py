import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
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
    f_name = models.CharField("first name", max_length=255)
    l_name = models.CharField("last name", max_length=255)
    phone = models.CharField("phone no.", max_length=255)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    tags = TaggableManager(through=UUIDTaggedItem)

    def __str__(self) -> str:
        return f'{self.f_name} Contact'
    
    def get_absolute_url(self):
        return reverse('contact-details', kwargs={'pk': self.pk})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        print(f'Current image path is: {self.image.path}')

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)