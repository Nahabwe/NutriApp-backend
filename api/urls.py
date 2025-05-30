from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'profiles', DiabetesProfileViewSet)
router.register(r'metrics', HealthMetricViewSet)
router.register(r'foods', FoodItemViewSet)
router.register(r'tips', HealthTipViewSet)
router.register(r'recipes', RecipeViewSet)

router.register(r'medication-answers', MedicationAnswerViewSet)
router.register(r'units', UnitPreferenceViewSet)
router.register(r'religion', ReligionPreferenceViewSet)
router.register(r'device', DevicePreferenceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
