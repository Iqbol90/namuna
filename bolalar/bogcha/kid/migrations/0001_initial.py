# Generated by Django 3.2.5 on 2021-07-18 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EatingTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('time', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('lastname', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('category', models.ManyToManyField(to='kid.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('drink', models.CharField(max_length=50, null=True)),
                ('day', models.CharField(max_length=50, null=True)),
                ('chef', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kid.staff')),
                ('time', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kid.eatingtime')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('number_of_children', models.IntegerField(null=True)),
                ('teacherName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kid.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Children',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('lastname', models.CharField(max_length=70, null=True)),
                ('age', models.IntegerField(null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kid.group')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=250, null=True)),
                ('body', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='kid.staff')),
            ],
        ),
    ]
