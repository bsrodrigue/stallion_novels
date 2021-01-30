# Generated by Django 3.1.2 on 2021-01-29 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0013_remove_chapter_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='novel',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]