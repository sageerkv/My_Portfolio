# Generated by Django 4.2 on 2023-07-22 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sageer_kv', '0023_skill'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='my_portfolio',
            name='about_link',
        ),
    ]