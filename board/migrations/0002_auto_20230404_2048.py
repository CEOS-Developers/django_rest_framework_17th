# Generated by Django 3.2.16 on 2023-04-04 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_media',
            name='post',
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Post_media',
        ),
    ]
