# Generated by Django 4.2.5 on 2023-12-13 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admuser', '0003_alter_articles_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='content',
        ),
    ]
