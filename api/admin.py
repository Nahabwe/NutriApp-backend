from django.contrib import admin
from django.contrib import admin
from .models import (
    DiabetesProfile, HealthMetric, FoodItem, HealthTip, Recipe,
    MedicationAnswer, UnitPreference, ReligionPreference, DevicePreference
)
@admin.register(DiabetesProfile)
class DiabetesProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'gender', 'diabet_type', 'diagnosis_date', 'created_at')
    search_fields = ('user__username', 'diabet_type')
    list_filter = ('gender', 'diabet_type')

@admin.register(HealthMetric)
class HealthMetricAdmin(admin.ModelAdmin):
    list_display = ('profile', 'fasting_glucose', 'hba1c', 'weight', 'bmi', 'created_at')
    search_fields = ('profile__user__username',)

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_url', 'created_at')
    search_fields = ('title',)

@admin.register(HealthTip)
class HealthTipAdmin(admin.ModelAdmin):
    list_display = ('title', 'nutritionist', 'created_at')
    search_fields = ('title', 'nutritionist')

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'calories', 'carbs')
    search_fields = ('name', 'category')
    list_filter = ('category',)

from django.contrib import admin
from .models import (
    DiabetesProfile, HealthMetric, FoodItem, HealthTip, Recipe,
    MedicationAnswer, UnitPreference, ReligionPreference, DevicePreference
)


@admin.register(MedicationAnswer)
class MedicationAnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'diabetes_type', 'takes_pills', 'created_at')
    search_fields = ('user__username', 'diabetes_type')
    list_filter = ('diabetes_type', 'takes_pills')

@admin.register(UnitPreference)
class UnitPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'unit', 'updated_at')
    search_fields = ('user__username', 'unit')
    list_filter = ('unit',)

@admin.register(ReligionPreference)
class ReligionPreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'religion', 'updated_at')
    search_fields = ('user__username', 'religion')
    list_filter = ('religion',)

@admin.register(DevicePreference)
class DevicePreferenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'device', 'updated_at')
    search_fields = ('user__username', 'device')
    list_filter = ('device',)