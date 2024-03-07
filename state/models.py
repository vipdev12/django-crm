from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Flat(models.Model):
    number = models.IntegerField(verbose_name='№ квартиры')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Объект')
    floor = models.IntegerField(verbose_name='Этаж')
    square = models.CharField(max_length=100, verbose_name='КВ')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    status = models.CharField(max_length=100, verbose_name='Статус')
    price = models.CharField(max_length=100, verbose_name='Цена')
    client = models.CharField(max_length=100, null=True, blank=True, default='-', verbose_name='Клиент')
    flat_status = models.CharField(max_length=100, default='-', null=True, blank=True, verbose_name='Статус')
    client_number = models.CharField(max_length=100, null=True, blank=True, default='-', verbose_name='Номер клиента')
    contract_number = models.IntegerField(verbose_name='№ Договора', null=True, blank=True)

    def __str__(self):
        return f'№ {str(self.number)}'


class Manager(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    phone_number = models.CharField(max_length=100, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Почта')
    date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    quantity_sell = models.IntegerField(verbose_name='Кол-во сделок', null=True, blank=True, default=0)
    password = models.CharField(max_length=100, null=True, blank=True, verbose_name='Временный пароль')


