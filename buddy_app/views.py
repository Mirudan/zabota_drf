from rest_framework import generics
from .models import Pet
from .serializers import PetSerializer


class PetCreateView(generics.CreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetListView(generics.ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetDetailView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class PetUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
