# Generated by Django 3.1 on 2020-08-11 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='series',
            old_name='descripion',
            new_name='description',
        ),
    ]