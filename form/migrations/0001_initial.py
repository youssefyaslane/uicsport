# Generated by Django 4.2.1 on 2023-06-20 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
                ('discipline', models.CharField(choices=[('foot', 'Football'), ('basket', 'Basketball'), ('tennis', 'Tennis')], max_length=10)),
            ],
        ),
    ]