# Generated by Django 3.0.8 on 2020-08-01 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchApi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(default=None)),
                ('product_name', models.CharField(max_length=255)),
                ('image_file', models.ImageField(upload_to='images/')),
                ('image_url', models.URLField()),
            ],
        ),
    ]