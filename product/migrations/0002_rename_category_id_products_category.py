# Generated by Django 3.2 on 2021-04-29 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='category_id',
            new_name='category',
        ),
    ]