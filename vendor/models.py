##############################################################################
# Модели для приложения Звено сети (vendor)
##############################################################################
from django.core.exceptions import ValidationError
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Vendor(models.Model):
    """
    Класс-модель, описывающий звено сети:
    level - уровень (завод, розница, ИП); (Надо ли?);
    name - название;
    contacts - контакты, ссылка на модель Contacts;
    products - продукция, ссылка на модель Products;
    vendor - Поставщик (предыдущий по иерархии объект сети);
    debt - Задолженность перед поставщиком в денежном выражении с точностью
    до копеек;
    date_create - Время создания (заполняется автоматически при создании).
    """

    FACTORY = 0
    RETAIL_NETWORK = 1
    INDIVIDUAL_ENTREPRENEUR = 2

    LEVEL_TYPE = (
        (FACTORY, 'Завод'),
        (RETAIL_NETWORK, 'Розничная сеть'),
        (INDIVIDUAL_ENTREPRENEUR, 'Индивидуальный предприниматель')
    )

    name = models.CharField(max_length=100, verbose_name='Название')
    seller_type = models.PositiveIntegerField(
        choices=LEVEL_TYPE, verbose_name='Тип', default=FACTORY
    )
    level = models.PositiveIntegerField(verbose_name='Уровень', default=0)
    contacts = models.ForeignKey(
        to='contacts.Contacts',
        on_delete=models.CASCADE,
        verbose_name='Контакты'
    )
    products = models.ManyToManyField(
        to='products.Product',
        verbose_name='Продукция'
    )
    vendor = models.ForeignKey(to='self', on_delete=models.SET_NULL,
                               verbose_name='Поставщик',
                               related_name='vendor_up',
                               **NULLABLE)
    debt = models.DecimalField(
        max_digits=9, decimal_places=2, default=0,
        verbose_name='Задолженность перед поставщиком', **NULLABLE
    )
    date_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания'
    )

    def __str__(self):
        # Строковое отображение звена цепи
        return f'{self.level} {self.name} (создано {self.date_create})'

    class Meta:
        verbose_name = 'объект'  # Настройка наименования одного объекта
        verbose_name_plural = 'объекты'  # Настройка для наименования набора
        ordering = ('name',)

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        if self.seller_type == 0 and self.level != 0:
            raise ValidationError('У завода может быть только уровень 0!')
        if self.seller_type != 0 and self.level == 0:
            raise ValidationError('Уровень 0 может быть только у завода!')
        # любой объект, кроме завода, должен иметь поставщика
        if self.seller_type != 0 and self.vendor is None:
            raise ValidationError('Укажите поставщика!')
        if self.vendor and self.level != (self.vendor.level + 1):
            raise ValidationError('Уровень объекта должен быть на 1 выше, '
                                  'чем уровень поставщика')
        # у завода не может быть задолженности перед поставщиком
        if self.seller_type == 0 and self.debt != 0:
            raise ValidationError('У завода не может быть задолженности '
                                  'перед поставщиком')
        if self.debt < 0:
            raise ValidationError('Сумма задолженности должна быть '
                                  'положительным числом')
