# Generated by Django 4.2.13 on 2024-05-24 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maths', '0003_result_result_maths_result_value_error_together_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='math',
            options={'ordering': ['-id']},
        ),
    ]
