# Generated by Django 4.1 on 2022-08-25 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0003_alter_user_gender"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="gender",
            field=models.CharField(default="Others", max_length=10),
        ),
    ]
