# Generated by Django 3.2.6 on 2021-08-22 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_customer_profilepicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profilePicture',
            field=models.ImageField(blank=True, default='img_avatar1.png', null=True, upload_to=''),
        ),
    ]
