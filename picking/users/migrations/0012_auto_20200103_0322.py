# Generated by Django 2.2.6 on 2020-01-02 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20200103_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('not-specified', 'Not Specified'), ('male', 'Male'), ('female', 'Female')], max_length=80, null=True),
        ),
    ]