# Generated by Django 3.2 on 2021-04-24 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group_assign_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobads',
            name='employer',
            field=models.CharField(max_length=100),
        ),
    ]
