# Generated by Django 3.2.6 on 2022-04-15 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_productcategories_is_valid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productcategories',
            old_name='is_valid',
            new_name='is_active',
        ),
    ]
