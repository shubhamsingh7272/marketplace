# Generated by Django 5.1.4 on 2024-12-18 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='This is a product'),
        ),
        migrations.AddField(
            model_name='shop',
            name='address',
            field=models.CharField(default='Default Product', max_length=255),
            preserve_default=False,
        ),
    ]
