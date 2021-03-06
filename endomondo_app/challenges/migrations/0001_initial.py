# Generated by Django 3.0.6 on 2020-05-28 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endomondo_id', models.IntegerField(unique=True)),
                ('title', models.CharField(blank=True, max_length=200)),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='Start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='End date')),
                ('parse_error', models.NullBooleanField()),
                ('status_text', models.CharField(default='-', max_length=200)),
                ('parse_date', models.DateTimeField(blank=True, null=True, verbose_name='Parse date')),
            ],
        ),
        migrations.CreateModel(
            name='Competitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endomondo_id', models.IntegerField(unique=True)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('display_name', models.CharField(blank=True, help_text='Optional, name will be parsed form endomondo.com if not specified', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenges.Challenge')),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories', models.IntegerField()),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenges.Challenge')),
                ('competitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenges.Competitor')),
            ],
        ),
        migrations.AddField(
            model_name='competitor',
            name='teams',
            field=models.ManyToManyField(blank=True, to='challenges.Team'),
        ),
    ]
