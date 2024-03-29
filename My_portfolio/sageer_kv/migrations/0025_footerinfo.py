# Generated by Django 4.2 on 2023-07-24 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sageer_kv', '0024_remove_my_portfolio_about_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('fb_link', models.URLField(blank=True)),
                ('insta_link', models.URLField(blank=True)),
                ('lnkdn_link', models.URLField(blank=True)),
                ('gtb_link', models.URLField(blank=True)),
                ('twtr_link', models.URLField(blank=True)),
            ],
        ),
    ]
