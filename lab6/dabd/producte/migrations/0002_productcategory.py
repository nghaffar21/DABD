# Generated by Django 5.2 on 2025-04-15 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producte', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cat_pare', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='producte.productcategory')),
                ('templates', models.ManyToManyField(blank=True, null=True, to='producte.producttemplate')),
            ],
        ),
    ]
