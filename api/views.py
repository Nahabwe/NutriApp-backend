from rest_framework import viewsets
from .models import DiabetesProfile, HealthMetric, FoodItem, HealthTip
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner

class DiabetesProfileViewSet(viewsets.ModelViewSet):
    permission_classes=[IsAuthenticated,IsOwner]
    queryset = DiabetesProfile.objects.all()
    serializer_class = DiabetesProfileSerializer

    def get_queryset(self):
        return DiabetesProfile.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

class HealthMetricViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsOwner]
    queryset = HealthMetric.objects.all()
    serializer_class = HealthMetricSerializer

    def get_queryset(self):
        return HealthMetric.objects.filter(profile__user=self.request.user)

    def perform_create(self, serializer):
        profile=DiabetesProfile.objects.get(user=self.request.user)
        serializer.save(profile=profile)

class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
 

class HealthTipViewSet(viewsets.ModelViewSet):
    queryset = HealthTip.objects.all()
    serializer_class = HealthTipSerializer
  

   

class RecipeViewSet(viewsets.ModelViewSet):
    queryset=Recipe.objects.all()
    serializer_class=RecipeSerializer
    
  

  
class MedicationAnswerViewSet(viewsets.ModelViewSet):
    serializer_class = MedicationAnswerSerializer
    queryset = MedicationAnswer.objects.all() 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MedicationAnswer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UnitPreferenceViewSet(viewsets.ModelViewSet):
    serializer_class = UnitPreferenceSerializer
    queryset = UnitPreference.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return UnitPreference.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReligionPreferenceViewSet(viewsets.ModelViewSet):
    serializer_class = ReligionPreferenceSerializer
    queryset = ReligionPreference.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ReligionPreference.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class DevicePreferenceViewSet(viewsets.ModelViewSet):
    serializer_class = DevicePreferenceSerializer
    queryset = DevicePreference.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return DevicePreference.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)