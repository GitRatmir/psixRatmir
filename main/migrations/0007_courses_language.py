# Generated by Django 3.1.4 on 2020-12-13 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201213_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='language',
            field=models.CharField(blank=True, max_length=150, verbose_name='Язык'),
        ),
    ]
