# Generated by Django 4.1.3 on 2022-12-20 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_company_alter_order_product_delete_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='cgpa',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='usn',
            field=models.IntegerField(default=0),
        ),
    ]