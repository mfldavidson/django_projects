# Generated by Django 2.2.1 on 2019-06-06 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0002_auto_20190605_1814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='iso',
            old_name='states_id',
            new_name='states',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='iso_id',
            new_name='iso',
        ),
    ]
