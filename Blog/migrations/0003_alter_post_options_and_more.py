# Generated by Django 4.2.7 on 2024-01-06 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_post_counted_views_post_create_date_post_published_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['create_date']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='published',
            new_name='published_date',
        ),
    ]
