# Generated by Django 2.0.1 on 2018-02-06 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_page_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]