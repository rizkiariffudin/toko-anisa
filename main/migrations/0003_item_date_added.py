# Generated by Django 4.2.5 on 2023-09-17 09:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_item_delete_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
