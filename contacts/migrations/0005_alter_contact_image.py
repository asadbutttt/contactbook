# Generated by Django 4.1.7 on 2023-04-04 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_contact_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='media/profile_pics'),
        ),
    ]
