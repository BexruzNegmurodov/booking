# Generated by Django 4.2.2 on 2023-07-10 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment_parents_comment_comment_reply_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parents_comment',
        ),
    ]