# Generated by Django 4.2 on 2023-04-28 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sageer_kv', '0003_rename_sm_link1_my_portfolio_fb_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='my_portfolio',
            old_name='sm_gtb_link',
            new_name='gtb_link',
        ),
    ]