# Generated by Django 4.2.3 on 2023-08-12 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0004_county_alter_role_usertypename_state_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='useraddress',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('buildingname', models.TextField(max_length=10)),
                ('streetname', models.TextField(max_length=20)),
                ('pincode', models.CharField(max_length=50)),
                ('cityname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.city')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newapp.userdetail')),
            ],
        ),
    ]
