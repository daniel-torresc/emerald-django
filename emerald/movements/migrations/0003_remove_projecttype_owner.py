# Generated by Django 4.2.8 on 2024-01-17 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movements', '0002_alter_accounttype_options_alter_cardtype_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projecttype',
            name='owner',
        ),
    ]
