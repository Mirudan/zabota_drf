from rest_framework import serializers
from .models import Pet


class PetSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    end_treatment_method = serializers.SerializerMethodField()
    end_vaccine = serializers.SerializerMethodField()

    class Meta:
        model = Pet
        fields = ['id', 'name', 'birthdate', 'age', 'breed', 'color', 'owner', 'vacсine_name', 'start_vaccine',
                  'validity_period_vaccine', 'end_vaccine',
                  'treatment_method',
                  'start_treatment_method', 'validity_period_treatment', 'end_treatment_method']

    def get_age(self, obj):
        return obj.age()

    def get_end_treatment_method(self, obj):
        return obj.end_treatment_method()

    def get_end_vaccine(self, obj):
        return obj.end_vaccine()
