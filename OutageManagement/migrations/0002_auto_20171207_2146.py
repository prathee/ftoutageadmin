# Generated by Django 2.0 on 2017-12-07 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('OutageManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outage',
            name='Outage_ID',
            field=models.CharField(help_text='Enter Outage Servcie Name', max_length=200),
        ),
        migrations.AlterField(
            model_name='outage',
            name='Service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='OutageManagement.Outage_Service'),
        ),
    ]
