# Generated by Django 2.2.5 on 2019-09-11 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('rate_ratio', models.FloatField(default=1.1)),
                ('popularity', models.CharField(choices=[('LT', 'Lowest'), ('LW', 'Low'), ('MD', 'Medium'), ('HI', 'High'), ('HT', 'Highest')], default='MD', max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='industries.Category')),
            ],
            options={
                'verbose_name_plural': 'Sub Categories',
            },
        ),
    ]
