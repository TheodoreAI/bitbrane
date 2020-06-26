# Generated by Django 2.2.10 on 2020-06-26 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('about', models.TextField()),
                ('contact', models.CharField(max_length=200)),
            ],
        ),
    ]