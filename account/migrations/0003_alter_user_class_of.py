# Generated by Django 3.2.16 on 2023-05-02 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_delete_usermanager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='class_of',
            field=models.IntegerField(null=True, verbose_name='입학연도'),
        ),
    ]
