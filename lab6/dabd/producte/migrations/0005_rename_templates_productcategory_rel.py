# Generated by Django 5.2 on 2025-04-15 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producte', '0004_rename_cat_pare_productcategory_pare'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productcategory',
            old_name='templates',
            new_name='rel',
        ),
    ]
