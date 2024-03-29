# Generated by Django 4.2.6 on 2024-01-06 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university', models.CharField(max_length=1000)),
                ('description', models.TextField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('extra', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('description', models.TextField()),
                ('skills', models.TextField()),
                ('gitlink', models.URLField()),
                ('livelink', models.URLField()),
                ('certificatelink', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('P', 'programme'), ('T', 'technology')], default='P', max_length=1)),
                ('image', models.ImageField(upload_to='pics/')),
            ],
        ),
    ]
