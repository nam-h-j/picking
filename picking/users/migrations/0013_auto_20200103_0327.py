# Generated by Django 2.2.6 on 2020-01-02 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200103_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('not-specified', 'Not Specified'), ('male', 'Male')], max_length=80, null=True),
        ),
    ]
