# Generated by Django 3.2.16 on 2024-06-02 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0006_auto_20240531_1442'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Restoran',
            new_name='Restaurant',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='restoran',
            new_name='restaurant',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='restoran',
            new_name='restaurant',
        ),
    ]
