# Generated by Django 4.0.4 on 2022-05-12 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimestampedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now=True)),
                ('modificado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
