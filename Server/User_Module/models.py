from django.contrib.auth.models import AbstractUser
from django.db import models

from Product_Module.models import ProductModel


class UserModel(AbstractUser):
    active_code = models.CharField(max_length=10, default='', verbose_name='کد فعالسازی حساب کاربری')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.username


class CartModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.PROTECT, verbose_name='کاربر')
    product = models.ForeignKey(ProductModel, on_delete=models.PROTECT, verbose_name='محصول')
    count = models.IntegerField(default=1, verbose_name='تعداد')
    is_finished = models.BooleanField(default=False, verbose_name='نهایی شده / نهایی نشده')
    date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'

    def __str__(self):
        return self.product.name

