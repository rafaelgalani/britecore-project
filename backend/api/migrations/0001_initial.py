# Generated by Django 3.1.7 on 2021-03-13 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('field_type', models.TextField(choices=[('TEXT', 'Text'), ('NUMBER', 'Number'), ('DATE', 'Date'), ('ENUM', 'Enum')])),
            ],
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RiskType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RiskTypeDefaultField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.field')),
                ('risk_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.risktype')),
            ],
        ),
        migrations.CreateModel(
            name='RiskField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.field')),
                ('risk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.risk')),
            ],
        ),
        migrations.AddField(
            model_name='risk',
            name='risk_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.risktype'),
        ),
        migrations.CreateModel(
            name='FieldValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.TextField()),
                ('value', models.TextField()),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.field')),
            ],
        ),
        migrations.AddConstraint(
            model_name='risktypedefaultfield',
            constraint=models.UniqueConstraint(fields=('risk_type', 'field'), name='risk_type_default_field_primary_constraint'),
        ),
        migrations.AddConstraint(
            model_name='riskfield',
            constraint=models.UniqueConstraint(fields=('risk', 'field'), name='risk_field_primary_constraint'),
        ),
    ]
