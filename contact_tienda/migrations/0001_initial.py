# Generated by Django 3.2.2 on 2021-05-11 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_contact', models.TextField(max_length=30)),
                ('phone_contact', models.TextField(max_length=10)),
                ('email_contact', models.EmailField(max_length=254)),
            ],
        ),
    ]
