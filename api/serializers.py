from rest_framework import serializers
from .models import DiabetesProfile,HealthMetric,HealthTip,FoodItem,Recipe,MedicationAnswer,UnitPreference,ReligionPreference,DevicePreference

class DiabetesProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=DiabetesProfile
        fields='__all__'


class HealthMetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthMetric
        fields = '__all__'

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'

class HealthTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthTip
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields='__all__'


class MedicationAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationAnswer
        fields = '__all__'

class UnitPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitPreference
        fields = '__all__'

class ReligionPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReligionPreference
        fields = '__all__'

class DevicePreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevicePreference
        fields = '__all__'

        