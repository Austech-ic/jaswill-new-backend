# Generated by Django 4.0 on 2024-06-14 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_alter_blog_status_alter_propertylisting_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertylisting',
            name='category',
        ),
    ]