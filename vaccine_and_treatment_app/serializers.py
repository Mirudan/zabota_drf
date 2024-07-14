from rest_framework import serializers
from .models import VaccineRabies, Treatment


class VaccineRabiesSerializer(serializers.ModelSerializer):
    end_vaccine = serializers.SerializerMethodField()

    class Meta:
        model = VaccineRabies
        fields = ['id', 'vacсine_name', 'start_vaccine', 'validity_period_vaccine', 'end_vaccine', 'pet_name']

    def get_end_vaccine(self, obj):
        return obj.end_vaccine


class TreatmentSerializer(serializers.ModelSerializer):
    end_treatment = serializers.SerializerMethodField()

    class Meta:
        model = Treatment
        fields = ['id', 'treatment_type', 'treatment_name', 'start_treatment', 'validity_period_treatment',
                  'end_treatment', 'pet_name']

    def get_end_treatment(self, obj):
        return obj.end_treatment
