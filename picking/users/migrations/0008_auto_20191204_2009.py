# Generated by Django 2.2.6 on 2019-12-04 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20191108_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('not-specified', 'Not Specified'), ('male', 'Male')], max_length=80, null=True),
        ),
    ]
