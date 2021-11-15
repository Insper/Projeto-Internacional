# Generated by Django 3.2.8 on 2021-11-15 22:13

from django.db import migrations, models
import django.db.models.deletion
import inputs.myFields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('homeUniversity', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('professor', models.CharField(max_length=200)),
                ('ects', models.IntegerField()),
                ('duration', models.TimeField()),
                ('availability', inputs.myFields.Status(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='CourseDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dayOfTheWeek', inputs.myFields.DayOfTheWeekField(choices=[('Friday', 'Friday'), ('Monday', 'Monday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday'), ('Thursday', 'Thursday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday')], max_length=9)),
                ('hour', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField()),
                ('candidate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='timetable', to='inputs.candidate')),
                ('courses', models.ManyToManyField(to='inputs.Course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='dates',
            field=models.ManyToManyField(to='inputs.CourseDate'),
        ),
    ]
