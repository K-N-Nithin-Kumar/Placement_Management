# Generated by Django 4.1.3 on 2023-01-03 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_rename_order_application'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='price',
            new_name='cgpa',
        ),
    ]
