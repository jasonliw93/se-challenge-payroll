# Generated by Django 2.1.3 on 2018-11-23 02:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('wage', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_id', models.IntegerField()),
                ('employee_id', models.IntegerField()),
                ('hours_worked', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('job_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.JobGroup')),
            ],
        ),
    ]
