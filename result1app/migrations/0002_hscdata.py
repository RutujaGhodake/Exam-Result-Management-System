# Generated by Django 4.0 on 2023-05-05 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result1app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hscdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('htno', models.IntegerField()),
                ('english', models.IntegerField()),
                ('marathi', models.IntegerField()),
                ('math', models.IntegerField()),
                ('physics', models.IntegerField()),
                ('chemistry', models.IntegerField()),
                ('biology', models.IntegerField()),
            ],
        ),
    ]
