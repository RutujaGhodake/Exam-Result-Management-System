# Generated by Django 4.0 on 2023-05-09 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result1app', '0005_degree2data_degree3data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='btechdata',
            old_name='aca',
            new_name='ap',
        ),
        migrations.RenameField(
            model_name='btechdata',
            old_name='ai',
            new_name='cds',
        ),
        migrations.RenameField(
            model_name='btechdata',
            old_name='cd',
            new_name='cit',
        ),
        migrations.RenameField(
            model_name='btechdata',
            old_name='dcs',
            new_name='eng',
        ),
        migrations.RenameField(
            model_name='btechdata',
            old_name='mad',
            new_name='math',
        ),
        migrations.RenameField(
            model_name='btechdata',
            old_name='se',
            new_name='sdc',
        ),
    ]
