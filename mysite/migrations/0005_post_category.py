# Generated by Django 4.2.4 on 2023-12-13 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_rename_comment_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.TextField(null=True),
        ),
    ]