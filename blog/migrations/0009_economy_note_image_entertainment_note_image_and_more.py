# Generated by Django 4.0.4 on 2022-06-13 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_rename_salud_economy_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='economy',
            name='note_image',
            field=models.ImageField(blank=True, upload_to='Economy_image'),
        ),
        migrations.AddField(
            model_name='entertainment',
            name='note_image',
            field=models.ImageField(blank=True, upload_to='Entertainment_image'),
        ),
        migrations.AddField(
            model_name='health',
            name='note_image',
            field=models.ImageField(blank=True, upload_to='Healt_image'),
        ),
    ]
