# Generated by Django 4.0.4 on 2022-06-15 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_rename_note_image_economy_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='economy',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Economy_image'),
        ),
        migrations.AlterField(
            model_name='entertainment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Entertainment_image'),
        ),
        migrations.AlterField(
            model_name='health',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Healt_image'),
        ),
    ]
