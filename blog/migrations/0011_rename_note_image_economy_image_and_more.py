# Generated by Django 4.0.4 on 2022-06-15 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_economy_publish_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='economy',
            old_name='note_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='entertainment',
            old_name='note_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='health',
            old_name='note_image',
            new_name='image',
        ),
    ]