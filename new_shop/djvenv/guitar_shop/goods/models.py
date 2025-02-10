from django.db import models

class CategoryGoods(models.Model): # в моделе харянятся категории товаров

    category = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.category

class AllGoods(models.Model): # модель которая более подробно описывает товары в магазине так же есть индексация

    #-----------------------------------------------------------------------------------------------#
    #сюда возможно добавлю контекснтый менеджер для того что бы отключать товары которые отсутствуют#
    #-----------------------------------------------------------------------------------------------#

    all_goods = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique=True)
    availability = models.BooleanField(null=True)
    quantity = models.IntegerField()
    image = models.ImageField( upload_to='images/', null=True, default='no_photo.png')
    price = models.IntegerField()
    model_of_instrument = models.CharField(max_length=50, null=True)
    articul = models.CharField(max_length=15, null=True, unique=True)

    category_goods = models.ForeignKey(CategoryGoods, on_delete=models.CASCADE, related_name= 'goods_all')

    def save(self, *args, **kwargs):    # метод для валидации полей которые могут принять отрицательные значения
        if self.quantity < 0:
            raise ValueError('Количество не может быть отрицательным')
        if self.price < 0:
            raise ValueError('Цена не может быть отрицательной')
        super().save(*args, **kwargs)

    class Meta:

        ordering = ['-price']
        indexes =[models.Index(fields=['-price']), ]

    def __str__(self):
        return self.all_goods

class СharacteristicsOfInstruments(models.Model):
    # для гитары
    color = models.CharField(max_length=50, null=True)
    construction = models.CharField(max_length=50, null=True)
    soundboard = models.CharField(max_length=50, null=True)
    guitar_neck = models.CharField(max_length=50, null=True)
    fingerboard = models.IntegerField(null=True)
    guitar_scale = models.CharField(max_length=50, null=True)
    frets = models.IntegerField(null=True)
    pickups = models.CharField(max_length=50, null=True)
    color_accessories = models.CharField(max_length=50, null=True)
    guitar_bridge = models.CharField(max_length=50, null=True)
    pegs = models.CharField(max_length=50, null=True)
    year_release = models.IntegerField(null=True)
    country_release =  models.CharField(max_length=50, null=True)
    # для звукоснимателей
    guitar_pickup_type = models.CharField(max_length=50, null=True)
    size = models.CharField(max_length=50, null=True)
    resistance = models.CharField(max_length=50, null=True)
    # для усилителей
    built_in_effects = models.CharField(max_length=50, null=True)
    number_of_channels = models.IntegerField(null=True)
    effect_loop = models.CharField(max_length=50, null=True)
    headphone_output = models.CharField(max_length=50, null=True)
    combo_amplifier_type = models.IntegerField(null=True)
    number_of_speakers = models.CharField(max_length=50, null=True)
    # для процессоров и педалей
    effect_loop = models.CharField(max_length=50, null=True)
    expression_pedal = models.CharField(max_length=50, null=True)
    digital_interfaces = models.CharField(max_length=50, null=True)
    effect_type = models.CharField(max_length=50, null=True)
    # для комплектущих
    number_of_strings_in_the_setcombo_amplifier_type = models.IntegerField(null=True)
    tension = models.CharField(max_length=50, null=True)
    core = models.CharField(max_length=50, null=True)
    material = models.CharField(max_length=50, null=True)

    describtion = models.TextField(null=True)
    all_goods = models.ForeignKey(AllGoods, on_delete=models.CASCADE, related_name = 'describe')








