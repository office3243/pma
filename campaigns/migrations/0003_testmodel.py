# Generated by Django 2.2.5 on 2019-09-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_auto_20190912_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='campaigns/test_models/')),
                ('text', models.TextField(blank=True)),
            ],
        ),
    ]
