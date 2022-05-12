# Generated by Django 3.2 on 2021-07-08 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='replys',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='comment',
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ManyToManyField(related_name='cm_ps', to='home.posts'),
        ),
        migrations.AddField(
            model_name='reply',
            name='comment',
            field=models.ManyToManyField(related_name='parant_cm', to='home.comments'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='posts',
            name='slug',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]