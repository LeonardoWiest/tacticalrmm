# Generated by Django 3.0.6 on 2020-05-20 04:37

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('checks', '0002_auto_20200520_0115'), ('checks', '0003_auto_20200520_0435')]

    dependencies = [
        ('agents', '0002_agent_time_zone'),
        ('automation', '0001_initial'),
        ('checks', '0001_initial'),
        ('autotasks', '0002_automatedtask_script'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventLogCheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_type', models.CharField(choices=[('diskspace', 'Disk Space Check'), ('ping', 'Ping Check'), ('cpuload', 'CPU Load Check'), ('memory', 'Memory Check'), ('winsvc', 'Win Service Check'), ('script', 'Script Check'), ('eventlog', 'Event Log Check')], default='eventlog', max_length=30)),
                ('desc', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('log_name', models.CharField(choices=[('Application', 'Application'), ('System', 'System'), ('Security', 'Security')], default='Application', max_length=255)),
                ('event_id', models.IntegerField(default=0)),
                ('event_type', models.CharField(choices=[('INFO', 'Information'), ('WARNING', 'Warning'), ('ERROR', 'Error'), ('AUDIT_SUCCESS', 'Success Audit'), ('AUDIT_FAILURE', 'Failure Audit')], default='ERROR', max_length=255)),
                ('fail_when', models.CharField(choices=[('contains', 'Log contains'), ('not_contains', 'Log does not contain')], default='contains', max_length=255)),
                ('search_last_days', models.IntegerField(default=1)),
                ('status', models.CharField(choices=[('passing', 'Passing'), ('failing', 'Failing'), ('pending', 'Pending')], default='pending', max_length=30)),
                ('failures', models.PositiveIntegerField(default=1)),
                ('failure_count', models.PositiveIntegerField(default=0)),
                ('more_info', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('email_alert', models.BooleanField(default=False)),
                ('text_alert', models.BooleanField(default=False)),
                ('last_run', models.DateTimeField(blank=True, null=True)),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventlogchecks', to='agents.Agent')),
                ('policy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventlogchecks', to='automation.Policy')),
                ('task_on_failure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='eventlogtaskfailure', to='autotasks.AutomatedTask')),
            ],
        ),
        migrations.AlterField(
            model_name='cpuloadcheck',
            name='check_type',
            field=models.CharField(choices=[('diskspace', 'Disk Space Check'), ('ping', 'Ping Check'), ('cpuload', 'CPU Load Check'), ('memory', 'Memory Check'), ('winsvc', 'Win Service Check'), ('script', 'Script Check'), ('eventlog', 'Event Log Check')], default='cpuload', max_length=30),
        ),
        migrations.AlterField(
            model_name='diskcheck',
            name='check_type',
            field=models.CharField(choices=[('diskspace', 'Disk Space Check'), ('ping', 'Ping Check'), ('cpuload', 'CPU Load Check'), ('memory', 'Memory Check'), ('winsvc', 'Win Service Check'), ('script', 'Script Check'), ('eventlog', 'Event Log Check')], default='diskspace', max_length=30),
        ),
        migrations.AlterField(
            model_name='memcheck',
            name='check_type',
            field=models.CharField(choices=[('diskspace', 'Disk Space Check'), ('ping', 'Ping Check'), ('cpuload', 'CPU Load Check'), ('memory', 'Memory Check'), ('winsvc', 'Win Service Check'), ('script', 'Script Check'), ('eventlog', 'Event Log Check')], default='memory', max_length=30),
        ),
        migrations.AlterField(
            model_name='pingcheck',
            name='check_type',
            field=models.CharField(choices=[('diskspace', 'Disk Space Check'), ('ping', 'Ping Check'), ('cpuload', 'CPU Load Check'), ('memory', 'Memory Check'), ('winsvc', 'Win Service Check'), ('script', 'Script Check'), ('eventlog', 'Event Log Check')], default='ping', max_length=30),
        ),
        migrations.AlterField(
            model_name='scriptcheck',
            name='check_type',
            field=models.CharField(choices=[('diskspace', 'Disk Space Check'), ('ping', 'Ping Check'), ('cpuload', 'CPU Load Check'), ('memory', 'Memory Check'), ('winsvc', 'Win Service Check'), ('script', 'Script Check'), ('eventlog', 'Event Log Check')], default='script', max_length=30),
        ),
        migrations.AlterField(
            model_name='winservicecheck',
            name='check_type',
            field=models.CharField(choices=[('diskspace', 'Disk Space Check'), ('ping', 'Ping Check'), ('cpuload', 'CPU Load Check'), ('memory', 'Memory Check'), ('winsvc', 'Win Service Check'), ('script', 'Script Check'), ('eventlog', 'Event Log Check')], default='winsvc', max_length=30),
        ),
        migrations.CreateModel(
            name='EventLogCheckEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent', models.DateTimeField(auto_now=True)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checks.EventLogCheck')),
            ],
        ),
    ]
