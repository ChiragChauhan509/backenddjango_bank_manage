# Generated by Django 4.2.3 on 2023-08-12 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='Usertypename',
            field=models.CharField(choices=[('addmin', 'admin'), ('custmer', 'custmer'), ('user', 'user')], max_length=50),
        ),
    ]
