# Generated by Django 4.1 on 2022-08-25 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0005_rename_task_content_task_content_task_target_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task", name="content", field=models.CharField(max_length=200),
        ),
    ]
