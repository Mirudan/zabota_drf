from datetime import timedelta
from django.db import models

from buddy_app.models import Pet


class VaccineRabies(models.Model):
    """
    Вакцина от бешенства
    """
    vacсine_name = models.CharField(max_length=255, verbose_name='Название вакцины')
    start_vaccine = models.DateField(verbose_name='Дата вакцинации', null=True)
    validity_period_vaccine = models.IntegerField(verbose_name='Срок действия вакцины', default=0)
    pet_name = models.ForeignKey(Pet, on_delete=models.CASCADE, verbose_name='Имя питомца')

    def end_vaccine(self):
        """
        Рассчет даты окончания действия вакцины
        """
        return self.start_vaccine + timedelta(days=self.validity_period_vaccine)


class Treatment(models.Model):
    """
    Другие обработки
    """
    treatment_type = models.CharField(verbose_name='Тип обработки')
    treatment_name = models.CharField(verbose_name='Название препарата')
    start_treatment = models.DateField(verbose_name='Дата обработки')
    validity_period_treatment = models.IntegerField(verbose_name='Срок действия обработки', default=0)
    pet_name = models.ForeignKey(Pet, on_delete=models.CASCADE, verbose_name='Имя питомца')

    def end_treatment(self):
        """
        Рассчет даты окончания действия обработки
        """
        return self.start_treatment + timedelta(days=self.validity_period_treatment)
