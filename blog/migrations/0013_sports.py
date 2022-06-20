# Generated by Django 4.0.4 on 2022-06-20 13:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_economy_image_alter_entertainment_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('publish_date', models.DateField(default=django.utils.timezone.now)),
                ('text', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Sports_image')),
            ],
            options={
                'verbose_name': 'Deporte',
                'verbose_name_plural': 'Deportes',
            },
        ),
    ]