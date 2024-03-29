# Generated by Django 2.2.5 on 2019-09-11 17:39

import campaigns.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('industries', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('localities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('default_font', models.CharField(blank=True, choices=[('AR', 'Arial'), ('CL', 'Calibari'), ('HL', 'Halvetica'), ('TR', 'Times Roman')], max_length=4)),
                ('default_font_size', models.CharField(blank=True, max_length=32)),
                ('order', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Entities',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('length', models.CharField(max_length=32)),
                ('height', models.CharField(max_length=32)),
                ('entities', models.ManyToManyField(to='campaigns.Entity')),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_id', models.CharField(blank=True, default=campaigns.models.unique_id_generator, max_length=64)),
                ('name', models.CharField(blank=True, max_length=64)),
                ('footer_file', models.FileField(upload_to='campaigns/footer_files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions='pdf')])),
                ('quantity', models.PositiveIntegerField(default=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('extra_charges', models.DecimalField(decimal_places=2, help_text='GST and other charges', max_digits=8)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('printed_copies', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('PP', 'Payment Pending'), ('DC', 'Declined'), ('NA', 'Not Approved'), ('AP', 'Approved'), ('RN', 'Running'), ('FN', 'Finished'), ('CN', 'Cancelled')], default='PP', max_length=2)),
                ('is_finished', models.BooleanField(default=False)),
                ('is_payed', models.BooleanField(default=False)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campaigns.Size')),
                ('sub_industry', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='industries.SubCategory')),
                ('sub_locality', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='localities.SubLocality')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
