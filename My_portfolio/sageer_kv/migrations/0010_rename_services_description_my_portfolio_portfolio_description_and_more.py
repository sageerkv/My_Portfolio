# Generated by Django 4.2 on 2023-04-30 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sageer_kv', '0009_my_portfolio_icon_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='my_portfolio',
            old_name='services_description',
            new_name='portfolio_description',
        ),
        migrations.RenameField(
            model_name='my_portfolio',
            old_name='services_head',
            new_name='portfolio_head',
        ),
        migrations.RenameField(
            model_name='my_portfolio',
            old_name='icon_link',
            new_name='portfolio_link',
        ),
        migrations.RemoveField(
            model_name='my_portfolio',
            name='services_link',
        ),
        migrations.AddField(
            model_name='my_portfolio',
            name='portfolio_img',
            field=models.ImageField(default=1, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
