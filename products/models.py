##############################################################################
# Модели для приложения Продукты (products)
##############################################################################
from django.db import models


class Product(models.Model):
    """
    Класс-модель, описывающий некий продукт:
    name- название;
    model - модель;
    date_release - дата выхода продукта на рынок.
    Все поля обязательные.
    """

    name = models.CharField(max_length=100, verbose_name='Название продукта')
    model = models.TextField(verbose_name='Описание продукта')
    date_release = models.DateTimeField(
        verbose_name='Дата выхода продукта на рынок'
    )

    def __str__(self):
        # Строковое отображение продукта
        return f'{self.name} {self.model} {self.date_release}'

    class Meta:
        verbose_name = 'продукт'  # Настройка наименования одного объекта
        verbose_name_plural = 'продукты'  # Настройка для наименования набора
        ordering = ('name',)
