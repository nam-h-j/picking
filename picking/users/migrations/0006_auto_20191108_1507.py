# Generated by Django 2.2.6 on 2019-11-08 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20191108_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('not-specified', 'Not Specified'), ('male', 'Male'), ('female', 'Female')], max_length=80, null=True),
        ),
    ]
