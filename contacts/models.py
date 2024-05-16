##############################################################################
# Модели для приложения Контакты (contacts)
##############################################################################
from django.db import models


class Contacts(models.Model):
    """
    Класс, описывающий Контакты поставщика:
    email - электронный адрес;
    country - страна;
    city - город;
    street - улица;
    house - номер дома.
    Все поля обязательные.
    """

    email = models.EmailField(verbose_name='электронная почта', unique=True)
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    house = models.CharField(max_length=10, verbose_name='номер дома')

    def __str__(self):
        # Строковое отображение адреса поставщика
        return (f'Адрес: {self.country}, {self.city}, \n '
                f'{self.street}, {self.house}\n {self.email}')

    class Meta:
        verbose_name = 'контакт'  # Настройка наименования одного объекта
        verbose_name_plural = 'контакты'  # Настройка для наименования набора
