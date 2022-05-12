# Generated by Django 3.2 on 2021-06-25 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='auth_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='djback.jpg', upload_to='')),
                ('name', models.CharField(default='', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_text', models.CharField(max_length=100)),
                ('c_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_text', models.CharField(max_length=100)),
                ('c_date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.auth_user')),
            ],
        ),
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('slug', models.CharField(max_length=30)),
                ('tag', models.CharField(max_length=100)),
                ('img', models.ImageField(default='', upload_to='')),
                ('date', models.DateField(auto_now_add=True)),
                ('popular', models.BooleanField(default=False)),
                ('views', models.IntegerField(default=0)),
                ('comment', models.ManyToManyField(related_name='commets', to='home.comments')),
                ('like', models.ManyToManyField(related_name='posts_llll', to='home.auth_user')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.auth_user')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='replys',
            field=models.ManyToManyField(related_name='commets', to='home.reply'),
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.auth_user'),
        ),
    ]
