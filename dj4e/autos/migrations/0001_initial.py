# Generated by Django 2.2.3 on 2019-07-05 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a make of a car', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200)),
                ('mileage', models.PositiveIntegerField()),
                ('comments', models.CharField(max_length=300)),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autos.Make')),
            ],
        ),
    ]
