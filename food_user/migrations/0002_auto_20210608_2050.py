# Generated by Django 3.2.4 on 2021-06-08 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooduser',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='fooduser',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='last_name'),
        ),
    ]
