# Generated by Django 2.2.5 on 2020-04-20 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercato_API', '0004_auto_20200419_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]
