# Generated by Django 4.1 on 2022-08-25 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0002_user_password_user_gender_user_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
