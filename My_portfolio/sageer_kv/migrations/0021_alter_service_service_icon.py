# Generated by Django 4.2 on 2023-07-20 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sageer_kv', '0020_alter_service_service_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_icon',
            field=models.CharField(choices=[('bx bx-code-alt', 'Web Development'), ('bx bxs-paint', 'Graphic Design'), ('bx code-block', 'Power apps')], max_length=50),
        ),
    ]