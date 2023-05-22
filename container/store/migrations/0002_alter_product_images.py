# Generated by Django 4.2.1 on 2023-05-16 16:53

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(upload_to=store.models.get_image_upload_path),
        ),
    ]