# Generated by Django 3.1.7 on 2021-07-16 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorymanagement', '0004_auto_20210715_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(blank=True, null=True, upload_to='Category'),
        ),
    ]