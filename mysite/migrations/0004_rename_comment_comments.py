# Generated by Django 4.2.4 on 2023-11-29 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_product_rename_time_comment_pub_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Comments',
        ),
    ]
