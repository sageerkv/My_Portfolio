# Generated by Django 4.2 on 2023-07-18 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sageer_kv', '0014_project_remove_my_portfolio_porject_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_icon', models.CharField(max_length=50)),
                ('service_title', models.CharField(max_length=100)),
                ('service_description', models.TextField()),
                ('service_link', models.URLField(blank=True, db_index=True, max_length=128, unique=True)),
            ],
        ),
    ]
