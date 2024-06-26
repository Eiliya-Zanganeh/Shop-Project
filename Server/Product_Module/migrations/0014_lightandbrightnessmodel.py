# Generated by Django 5.0.4 on 2024-06-26 17:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product_Module', '0013_delete_lightandbrightnessmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='LightAndBrightnessModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='نام کالا')),
                ('image', models.ImageField(upload_to='products/', verbose_name='عکس کالا')),
                ('price', models.DecimalField(decimal_places=0, max_digits=15, verbose_name='قیمت محصول')),
                ('offer_price', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True, verbose_name='قیمت پس از تخفیف')),
                ('offer', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='درصد تخفیف')),
                ('buy_count', models.PositiveIntegerField(default=0, verbose_name='تعداد فروش')),
                ('description', models.TextField(blank=True, null=True, verbose_name='توضیحات یا جزئیات')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='تعداد در انبار')),
                ('visits', models.PositiveIntegerField(default=0, verbose_name='تعداد بازدید')),
                ('category', models.CharField(choices=[('lamps_and_lights', 'لامپ و چراغ'), ('projector', 'پروژکتور'), ('moonlight_and_bracket', 'مهتابی و براکت'), ('flashlight_and_headlight', 'چراغ قوه و هدلایت'), ('Reading_light_and_sleeping_light', 'چراغ مطالعه و چراغ خواب')], max_length=35, verbose_name='دسته بندی')),
                ('watt', models.IntegerField(blank=True, null=True, verbose_name='وات')),
                ('frequency', models.IntegerField(blank=True, null=True, verbose_name='فرکانس')),
                ('hinge', models.FloatField(blank=True, null=True, verbose_name='شارنوری')),
            ],
            options={
                'verbose_name': 'نور و روشنایی',
                'verbose_name_plural': 'نور و روشنایی',
                'db_table': 'light_and_brightness',
            },
        ),
    ]
