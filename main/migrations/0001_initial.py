# Generated by Django 3.1.5 on 2021-01-30 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=100, verbose_name='Name')),
                ('body', models.TextField(verbose_name='Article')),
                ('date', models.DateTimeField(verbose_name='Time')),
            ],
        ),
    ]
