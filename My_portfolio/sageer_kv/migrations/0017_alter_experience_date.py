# Generated by Django 4.2 on 2023-07-18 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sageer_kv', '0016_date_alter_service_service_icon_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='date',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='sageer_kv.date'),
        ),
    ]
