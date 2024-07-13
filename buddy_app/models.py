from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class Pet(models.Model):
    """
    Модель питомца, со всеми данными
    """
    name = models.CharField(max_length=255, verbose_name='Кличка')
    birthdate = models.DateField(verbose_name='Дата рождения')
    breed = models.CharField(max_length=255, verbose_name='Порода')
    color = models.CharField(max_length=255, verbose_name='Окрас')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')
    vacсine_name = models.CharField(max_length=255, verbose_name='Название вакцины', null=True)
    start_vaccine = models.DateField(verbose_name='Дата вакцинации', null=True)
    validity_period_vaccine = models.IntegerField(verbose_name='Срок действия вакцины', default=0)
    treatment_method = models.CharField(max_length=255, verbose_name='Название обработки')
    start_treatment_method = models.DateField(verbose_name='Дата обработки')
    validity_period_treatment = models.IntegerField(verbose_name='Срок действия обработки', default=0)

    def __str__(self):
        return self.name

    def age(self):
        """
        Рассчет возраста
        """
        today = datetime.now().date()
        return today.year - self.birthdate.year - (
                (today.month, today.day) < (self.birthdate.month, self.birthdate.day))

    def end_treatment_method(self):
        """
        Рассчет даты окончания действия обработки
        """
        return self.start_treatment_method + timedelta(days=self.validity_period_treatment)

    def end_vaccine(self):
        """
        Рассчет даты окончания действия вакцины
        """
        return self.start_vaccine + timedelta(days=self.validity_period_vaccine)
