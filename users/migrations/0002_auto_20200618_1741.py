# Generated by Django 3.0.7 on 2020-06-18 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regdoctor',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='regdoctor',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='regpatient',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
