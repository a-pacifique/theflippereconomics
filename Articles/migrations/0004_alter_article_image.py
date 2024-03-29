# Generated by Django 4.2.4 on 2024-03-13 17:24

import Articles.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Articles', '0003_alter_article_options_article_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=Articles.models.ResizedImageField(upload_to='articles/images/', verbose_name='article image'),
        ),
    ]
