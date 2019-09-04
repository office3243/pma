# Generated by Django 2.2.5 on 2019-09-04 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('localities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('short_name', models.CharField(blank=True, max_length=6)),
                ('extra_info', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='extra_info',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='locality',
            name='extra_info',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='localities.State'),
            preserve_default=False,
        ),
    ]
