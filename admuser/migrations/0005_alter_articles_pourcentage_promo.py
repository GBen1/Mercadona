# Generated by Django 4.2.5 on 2023-12-13 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admuser', '0004_remove_articles_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='pourcentage_promo',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
