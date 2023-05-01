# Generated by Django 4.1.7 on 2023-04-30 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(error_messages={'unique': 'This email is already taken.'}, max_length=255, unique=True, verbose_name='email address'),
        ),
    ]