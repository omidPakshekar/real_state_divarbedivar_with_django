# Generated by Django 3.0.5 on 2020-05-11 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200511_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='file_number',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
