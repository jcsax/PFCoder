# Generated by Django 4.0.4 on 2022-06-23 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_contacto_alter_users_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contacto',
            new_name='Contact',
        ),
    ]
