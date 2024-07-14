from rest_framework import serializers
from .models import Pet


class PetSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = ['id', 'pets_name', 'type_of_pet', 'birthdate', 'age', 'breed', 'color', 'owner']

    def get_age(self, obj):
        return obj.age()
