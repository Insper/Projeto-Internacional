# Generated by Django 3.0 on 2021-12-15 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputs', '0002_remove_candidate_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
