# Generated by Django 4.2.11 on 2024-05-29 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=30),
        ),
    ]
