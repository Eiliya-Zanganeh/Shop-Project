from django.db import models
from Product_Module.models import ProductModel


class SiteSettingModel(models.Model):
    site_name = models.CharField(max_length=300, verbose_name='نام سایت')
    site_description = models.CharField(max_length=300, verbose_name='توضیحات سایت')
    description_img = models.ImageField(upload_to='description_img/', verbose_name='عکس توضیحات سایت')
    popular_products = models.ManyToManyField(ProductModel, related_name='popular_products',
                                              verbose_name='محصولات ویژه')

    class HowActiveUserAccount(models.TextChoices):
        email = ("email", "ایمیل")
        phone = ("phone", "شماره تلفن")

    how_active_user_account = models.CharField(max_length=10, choices=HowActiveUserAccount, default='email',
                                               verbose_name='شیوه فعال سازی حساب کاربری')

    is_active = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات های سایت'
        ordering = ['is_active']
        db_table = 'site_setting'

    def __str__(self):
        return self.site_name
