# Generated by Django 5.0.6 on 2024-05-20 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.CharField(default='riaan', max_length=30),
            preserve_default=False,
        ),
    ]
