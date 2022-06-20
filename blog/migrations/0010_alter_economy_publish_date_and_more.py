# Generated by Django 4.0.4 on 2022-06-14 22:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_economy_note_image_entertainment_note_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='economy',
            name='publish_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='entertainment',
            name='publish_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='health',
            name='publish_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]