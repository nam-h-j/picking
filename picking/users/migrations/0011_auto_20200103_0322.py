# Generated by Django 2.2.6 on 2020-01-02 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200103_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('not-specified', 'Not Specified'), ('female', 'Female')], max_length=80, null=True),
        ),
    ]