# Generated by Django 2.2.5 on 2020-11-25 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20201125_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='post_type',
            field=models.ManyToManyField(blank=True, related_name='blogs', to='blogs.PostType'),
        ),
    ]