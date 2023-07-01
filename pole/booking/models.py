from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime
from django.contrib.auth.models import User, Group


# Create your models here.

class Region(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название района')
    slug = models.SlugField(unique=True, null=True)

    def get_absolute_url(self):
        return reverse('filter', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'
        ordering = ['pk']


class Field(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name='Название поля')
    price = models.IntegerField(verbose_name='Цена поля на час')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    phone = PhoneNumberField(null=False, blank=False, unique=True, verbose_name='Телефонный номер владельца')
    lenght = models.IntegerField(default=0, verbose_name='Длина')
    width = models.IntegerField(default=0, verbose_name='Ширина')
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Район', related_name='fields')
    adress = models.CharField(max_length=250, default='Ташкент', verbose_name='Адрес')
    adress_url = models.URLField(max_length=300, verbose_name='Адрес URL', default='https://yandex.uz/maps/10335/tashkent/?ll=69.279737%2C41.311151&z=12')
    adress_coordinates = models.CharField(max_length=50, verbose_name='Кординаты адреса поля', default='41.311151, 69.279716')
    slug = models.SlugField(unique=True, null=True)

    def get_absolute_url(self):
        return reverse('field_detail', kwargs={'slug': self.slug})

    def get_first_image(self):
        if self.images:
            try:
                return self.images.all()[0].image.url
            except:
                return 'https://jutagrass.com.ua/wp-content/uploads/2019/09/futbolnoe-pole-razmeryi-i-razmetka-standartyi-fifa-2019-2-418x315.jpg'
        else:
            return 'https://jutagrass.com.ua/wp-content/uploads/2019/09/futbolnoe-pole-razmeryi-i-razmetka-standartyi-fifa-2019-2-418x315.jpg'

    def __str__(self):
        return self.title

    def __repr__(self):
        return f'Field (pk={self.pk}, title={self.title}, price={self.price})'

    class Meta:
        verbose_name = 'Поле'
        verbose_name_plural = 'Поля'
        ordering = ['-created_at', 'region']


class Gallery(models.Model):
    image = models.ImageField(upload_to='field/', verbose_name='Изображение')
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Галерея полей'


TIME_CHOICES = (
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
    ("13", "13"),
    ("14", "14"),
    ("15", "15"),
    ("16", "16"),
    ("17", "17"),
    ("18", "18"),
    ("19", "19"),
    ("20", "20"),
    ("21", "21"),
    ("22", "22"),
    ("23", "23"),
)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    field = models.ForeignKey(Field, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField()
    time = models.CharField(max_length=10, choices=TIME_CHOICES)
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.user.username} | day: {self.date} | time: {self.time}"

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'
        unique_together = ('date', 'time', 'field')