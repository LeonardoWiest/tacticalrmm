# Generated by Django 3.1.4 on 2021-02-12 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0004_auto_20210212_1408'),
        ('clients', '0008_auto_20201103_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='alert_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clients', to='alerts.alerttemplate'),
        ),
        migrations.AddField(
            model_name='site',
            name='alert_template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sites', to='alerts.alerttemplate'),
        ),
    ]
