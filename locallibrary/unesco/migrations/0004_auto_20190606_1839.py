# Generated by Django 2.2.1 on 2019-06-06 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0003_auto_20190606_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iso',
            name='states',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unesco.States'),
        ),
    ]
