# Generated by Django 3.1.7 on 2021-08-20 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210726_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.DateField(default=0),
            preserve_default=False,
        ),
    ]