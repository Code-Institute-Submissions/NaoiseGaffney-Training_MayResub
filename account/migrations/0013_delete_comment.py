# Generated by Django 3.1.7 on 2021-03-11 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_remove_comment_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
