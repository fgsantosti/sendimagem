# Generated by Django 3.0a1 on 2019-11-22 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('imagem', models.ImageField(upload_to='blog/media')),
                ('data', models.DateField()),
                ('text', models.TextField()),
            ],
        ),
    ]
