# Generated by Django 4.1.3 on 2022-12-29 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_rename_address_order_profile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Application',
        ),
    ]