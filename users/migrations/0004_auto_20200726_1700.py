# Generated by Django 3.0.8 on 2020-07-26 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200726_1634'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='total_comments',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='total_reactions',
        ),
    ]