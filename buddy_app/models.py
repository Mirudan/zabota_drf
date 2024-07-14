from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Pet(models.Model):
    """
    Модель питомца
    """
    pets_name = models.CharField(max_length=255, verbose_name='Кличка')
    type_of_pet = models.CharField(max_length=255, verbose_name='Вид питомца', null=True)
    birthdate = models.DateField(verbose_name='Дата рождения')
    breed = models.CharField(max_length=255, verbose_name='Порода')
    color = models.CharField(max_length=255, verbose_name='Окрас')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')
    treatment_method = models.CharField(max_length=255, verbose_name='Название обработки')
    start_treatment_method = models.DateField(verbose_name='Дата обработки')
    validity_period_treatment = models.IntegerField(verbose_name='Срок действия обработки', default=0)

    def __str__(self):
        return self.pets_name

    def age(self):
        """
        Рассчет возраста
        """
        today = datetime.now().date()
        return today.year - self.birthdate.year - (
                (today.month, today.day) < (self.birthdate.month, self.birthdate.day))
