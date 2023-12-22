# Generated by Django 4.2.4 on 2023-08-26 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('count_of_programs', models.PositiveSmallIntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
                ('year', models.PositiveSmallIntegerField()),
                ('max', models.PositiveSmallIntegerField()),
                ('min', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('duration', models.CharField(max_length=100)),
                ('requirements', models.JSONField()),
                ('faculty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.faculty')),
                ('grant_code', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='guide.grant')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.JSONField()),
                ('number', models.CharField(max_length=20)),
                ('site', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('dormitary', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('program_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.program')),
            ],
        ),
        migrations.AddField(
            model_name='faculty',
            name='univ_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.university'),
        ),
    ]
