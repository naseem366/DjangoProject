# Generated by Django 3.1.7 on 2021-06-11 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorymanagement', '0002_auto_20210611_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
