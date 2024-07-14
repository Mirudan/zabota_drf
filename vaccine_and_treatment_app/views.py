from rest_framework import generics
from .models import VaccineRabies, Treatment
from .serializers import VaccineRabiesSerializer, TreatmentSerializer


class VaccineRabiesList(generics.ListAPIView):
    """
    Все сделанные вакцины от бешенства
    """
    queryset = VaccineRabies.objects.all()
    serializer_class = VaccineRabiesSerializer


class VaccineRabiesCreate(generics.RetrieveAPIView):
    """
    Создание записи о вакцине от бешенства
    """
    queryset = VaccineRabies.objects.all()
    serializer_class = VaccineRabiesSerializer


class VaccineRabiesUpdate(generics.RetrieveUpdateAPIView):
    """
    Чтение и изменение конкретной записи
    """
    queryset = VaccineRabies.objects.all()
    serializer_class = VaccineRabiesSerializer


class VaccineRabiesDelete(generics.RetrieveDestroyAPIView):
    """
    Чтение и удаление записи
    """
    queryset = VaccineRabies.objects.all()
    serializer_class = VaccineRabiesSerializer


class TreatmentList(generics.ListAPIView):
    """
    Список обработок
    """
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer


class TreatmentCreate(generics.RetrieveAPIView):
    """
    Создание записи об обработке
    """
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer


class TreatmentUpdate(generics.RetrieveUpdateAPIView):
    """
    Чтение и обновление записи
    """
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer


class TreatmentDelete(generics.RetrieveDestroyAPIView):
    """
    Чтение и удаление записи
    """
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
