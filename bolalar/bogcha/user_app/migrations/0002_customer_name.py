# Generated by Django 3.2.5 on 2021-07-27 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
