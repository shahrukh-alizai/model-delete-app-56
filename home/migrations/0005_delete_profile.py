# Generated by Django 2.2.16 on 2020-10-08 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_delete_student"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Profile",
        ),
    ]
