from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class ProductCategoryModel(models.Model):
    name = models.CharField(max_length=300, verbose_name='نام دسته بندی')
    image = models.ImageField(upload_to='product_category/', verbose_name='عکس دسته بندی')

    class Meta:
        verbose_name = 'دسته بندی محصولات'
        verbose_name_plural = 'دسته بندی های محصولات'
        ordering = ['name']
        db_table = 'product_category'

    def __str__(self):
        return self.name


class ProductModel(models.Model):
    name = models.CharField(max_length=300, verbose_name='نام کالا')
    image = models.ImageField(upload_to='products/', verbose_name='عکس کالا')
    price = models.DecimalField(max_digits=15, decimal_places=0, verbose_name='قیمت محصول')
    offer_price = models.DecimalField(max_digits=15, decimal_places=0, verbose_name='قیمت پس از تخفیف', null=True,
                                      blank=True)
    offer = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name='درصد تخفیف',
                                null=True, blank=True)
    category = models.ForeignKey(ProductCategoryModel, on_delete=models.CASCADE, verbose_name='دسته بندی محصول')
    buy_count = models.PositiveIntegerField(default=0, verbose_name='تعداد فروش')
    description = models.TextField(verbose_name='توضیحات')
    count = models.PositiveIntegerField(default=0, verbose_name='تعداد در انبار')
    visits = models.PositiveIntegerField(default=0, verbose_name='تعداد بازدید')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        ordering = ['id']
        db_table = 'product'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if (not self.offer) and (not self.offer_price):
            ...
        elif self.offer and self.offer_price:
            ...
        else:
            if self.offer == '' or self.offer is None:
                self.offer = 100 - (round(self.offer_price * 100 / self.price))
            elif self.offer_price == '' or self.offer_price is None:
                self.offer_price = self.price - (self.price * self.offer / 100)
        return super().save(args, kwargs)


class GalleryModel(models.Model):
    image = models.ImageField(upload_to='galleries/')
    product = models.ForeignKey(ProductModel, on_delete=models.PROTECT, verbose_name='کالا', related_name='galleries')

    class Meta:
        verbose_name = 'گالری محصول'
        verbose_name_plural = 'گالری محصولات'
        ordering = ['id']
        db_table = 'gallery'

    def __str__(self):
        return self.product.name
