# Generated by Django 4.0.6 on 2022-09-08 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
