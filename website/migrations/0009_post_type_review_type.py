# Generated by Django 4.0.2 on 2022-05-08 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_rename_time_created_review_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(default='post', max_length=7),
        ),
        migrations.AddField(
            model_name='review',
            name='type',
            field=models.CharField(default='review', max_length=7),
        ),
    ]
