# Generated by Django 4.0.5 on 2022-06-18 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New Task', max_length=30)),
                ('description', models.CharField(blank=True, default='', max_length=255)),
                ('state', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'tasks',
            },
        ),
    ]