# Generated by Django 4.1.3 on 2022-12-20 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_student_cgpa_student_usn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='price',
            new_name='cgpa',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='product',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address',
            new_name='profile',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customer',
            new_name='student',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
    ]
