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


class AbstractProduct(models.Model):
    name = models.CharField(max_length=300, verbose_name='نام کالا')
    image = models.ImageField(upload_to='products/', verbose_name='عکس کالا')
    price = models.DecimalField(max_digits=15, decimal_places=0, verbose_name='قیمت محصول')
    offer_price = models.DecimalField(max_digits=15, decimal_places=0, verbose_name='قیمت پس از تخفیف', null=True,
                                      blank=True)
    offer = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name='درصد تخفیف',
                                null=True, blank=True)
    category = models.ForeignKey(ProductCategoryModel, on_delete=models.CASCADE, verbose_name='دسته بندی محصول')
    buy_count = models.PositiveIntegerField(default=0, verbose_name='تعداد فروش')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات یا جزئیات')
    count = models.PositiveIntegerField(default=0, verbose_name='تعداد در انبار')
    visits = models.PositiveIntegerField(default=0, verbose_name='تعداد بازدید')

    class Meta:
        abstract = True


class LightAndBrightnessModel(AbstractProduct):
    class ProductCategory(models.TextChoices):
        lamps_and_lights = 'lamps_and_lights', 'لامپ و چراغ',
        projector = 'projector', 'پروژکتور',
        moonlight_and_bracket = 'moonlight_and_bracket', 'مهتابی و براکت',
        flashlight_and_headlight = 'flashlight_and_headlight', 'چراغ قوه و هدلایت',
        Reading_light_and_sleeping_light = 'Reading_light_and_sleeping_light', 'چراغ مطالعه و چراغ خواب'

    category = models.CharField(
        max_length=35,
        choices=ProductCategory.choices,
        verbose_name='دسته بندی'
    )
    watt = models.FloatField(null=True, blank=True, verbose_name='وات')
    frequency = models.FloatField(null=True, blank=True, verbose_name='فرکانس')
    # Todo: color
    hinge = models.FloatField(null=True, blank=True, verbose_name='شارنوری')

    # Todo: warranty

    class Meta:
        verbose_name = 'نور و روشنایی'
        verbose_name_plural = verbose_name
        db_table = 'light_and_brightness'

    def __str__(self):
        return self.name


class WireAndCableModel(AbstractProduct):
    size = models.FloatField(null=True, blank=True, verbose_name='سایز برحسب متر')
    # Todo: insulation
    # Todo: alloy
    voltage = models.FloatField(null=True, blank=True, verbose_name='ولتاژ')

    class Meta:
        verbose_name = 'سیم و کابل'
        verbose_name_plural = verbose_name
        db_table = 'wire_and_able'

    def __str__(self):
        return self.name


class SwitchesAndSocketsModel(AbstractProduct):
    # Todo: color
    voltage = models.FloatField(null=True, blank=True, verbose_name='ولتاژ')

    # Todo: quality

    class Meta:
        verbose_name = 'کلید و پریز'
        verbose_name_plural = verbose_name
        db_table = 'switches_and_sockets'

    def __str__(self):
        return self.name


class ProtectorAndTeeModel(AbstractProduct):
    class ProductCategory(models.TextChoices):
        protector = 'protector', 'محافظ',
        tee = 'tee', 'سه راهی',

    category = models.CharField(
        max_length=35,
        choices=ProductCategory.choices,
        verbose_name='دسته بندی'
    )
    outlet_count = models.IntegerField(null=True, blank=True, verbose_name='تعداد پریز')
    # Todo: quality
    # Todo: color
    power = models.FloatField(null=True, blank=True, verbose_name='توان')

    # Todo: warranty

    class Meta:
        verbose_name = 'محافظ و سه راهی',
        verbose_name_plural = verbose_name
        db_table = 'protector_and_tee'

    def __str__(self):
        return self.name


class AntennaModel(AbstractProduct):
    class ProductCategory(models.TextChoices):
        aerial = 'aerial', 'آنتن هوایی',
        desktop = 'desktop', 'آنتن رومیزی',

    category = models.CharField(
        max_length=35,
        choices=ProductCategory.choices,
        verbose_name='دسته بندی'
    )
    # Todo: quality
    # Todo: cable_series
    # Todo: color
    # Todo: warranty

    items_included_with_the_product = models.CharField(
        max_length=300,
        null=True,
        blank=True,
        verbose_name='اقلام همراه محصول'
    )

    class Meta:
        verbose_name = 'آنتن'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ControlModel(AbstractProduct):
    # Todo: brand

    class Meta:
        verbose_name = 'کنتزل'
        verbose_name_plural = verbose_name
        db_table = 'control'

    def __str__(self):
        return self.name


class BatteryModel(AbstractProduct):
    # Todo: brands
    voltage = models.FloatField(null=True, blank=True, verbose_name='ولتاژ')

    class Meta:
        verbose_name = 'باطری'
        verbose_name_plural = verbose_name
        db_table = 'battery'

    def __str__(self):
        return self.name


class BuildingEquipmentModel(AbstractProduct):
    class ProductCategory(models.TextChoices):
        duct = 'duct', 'داکت',
        key_box = 'key_box', 'قوطی کلید',
        junction_box = 'junction_box', 'جعبه تقسیم',
        fuse = 'Fuse', 'فیوز',
        electric_pipe_and_fittings = 'electric_pipe_and_fittings', 'لوله برق و اتصالات'

    category = models.CharField(
        max_length=35,
        choices=ProductCategory.choices,
        verbose_name='دسته بندی'
    )

    class Meta:
        verbose_name = 'لوازم ساختمانی'
        verbose_name_plural = verbose_name
        db_table = 'building_equipment'

    def __str__(self):
        return self.name


class EntryPhoneModel(AbstractProduct):
    number_of_units = models.IntegerField(null=True, blank=True, verbose_name='تعداد واحد')

    class Meta:
        verbose_name = 'آیفن'
        verbose_name_plural = verbose_name
        db_table = 'entry_phone'

    def __str__(self):
        return self.name


class MiscellaneousGoodsModel(AbstractProduct):
    class Meta:
        verbose_name = 'کالا متفرقه'
        verbose_name_plural = verbose_name
        db_table = 'Miscellaneous_goods'

    def __str__(self):
        return self.name
