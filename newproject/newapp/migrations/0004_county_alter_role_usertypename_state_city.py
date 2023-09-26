# Generated by Django 4.2.3 on 2023-08-12 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0003_userdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='county',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('countyname', models.CharField(choices=[('INDIA', 'INDIA'), ('america', 'america'), ('caneda', 'caneda')], max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='role',
            name='Usertypename',
            field=models.CharField(choices=[('admin', 'admin'), ('custmer', 'custmer'), ('user', 'user')], max_length=50),
        ),
        migrations.CreateModel(
            name='state',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('statename', models.CharField(choices=[('BHARAT', 'BHARAT'), ('BIHAR', 'BIHAR'), ('KASMIR', 'KSM')], max_length=50)),
                ('countyid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newapp.county')),
            ],
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cityname', models.CharField(choices=[('SURAT', 'SURAT'), ('BHAVNAGAR', 'BHAVNAGAR'), ('AMEDABAD', 'AMD')], max_length=50)),
                ('stateid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='newapp.state')),
            ],
        ),
    ]
