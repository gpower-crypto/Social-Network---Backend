# Generated by Django 4.2 on 2023-09-02 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_first_name_userprofile_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
