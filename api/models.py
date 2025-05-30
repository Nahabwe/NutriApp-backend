from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
import datetime


class DiabetesProfile(models.Model):
    GENDER_CHOICES=[
        ('Male','Male'),
        ('Female','Female'),
        ('Any','Any'),
       
    ]
    DIABETES_TYPES =[
        ('Type 1','Type 1'),
        ('Type 2','Type 2'),
        ('Gestational','Gestational'),
        ('All','All'),
    ]

    user=models.OneToOneField(User,on_delete=models.CASCADE)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
    diabet_type=models.CharField(max_length=20,choices=DIABETES_TYPES)
    diagnosis_date=models.DateField()

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.age < 0:
            raise ValidationError('Age cannot be negative')
        if self.diagnosis_date > datetime.date.today():
            raise ValidationError('Diagnosis date cannot be in the future')

    
    def __str__(self):
        return self.user.username

class HealthMetric(models.Model):
    profile=models.ForeignKey(DiabetesProfile,on_delete=models.CASCADE)
    fasting_glucose=models.CharField(max_length=20)
    hba1c=models.CharField(max_length=20)
    daily_carbs=models.CharField(max_length=20)
    weight=models.CharField(max_length=10)
    height=models.CharField(max_length=10)
    bmi=models.CharField(max_length=10)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        try:
            bmi_value=float(self.bmi)
            if bmi_value <=10 or bmi_value >=80:
                raise ValidationError({'bmi':'BMI value must be realistic (10-80).'})
        except ValueError:
            raise ValidationError({'bmi':'BMI value must be a number.'})

    def __str__(self):
        return f'Metrics for {self.profile.user.username}'

class FoodItem(models.Model):
    title=models.CharField(max_length=100)
    image_url=models.URLField()
    recipe=models.TextField()

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class HealthTip(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    nutritionist=models.CharField(max_length=100)
    image_url=models.URLField()

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class Recipe(models.Model):
    CATEGORY_CHOICES=[
        ('Breakfast','Breakfast'),
        ('Lunch','Lunch'),
        ('Supper','Supper'),
    ]
  
  
    name=models.CharField(max_length=100)
    video=models.URLField()
    description=models.TextField()
    suitable_for=models.CharField(max_length=100)
    category=models.CharField(max_length=20,choices=CATEGORY_CHOICES)
    calories=models.IntegerField()
    carbs=models.CharField(max_length=20)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class MedicationAnswer(models.Model):
    DIABETES_TYPES =[
        ('Type 1','Type 1'),
        ('Type 2','Type 2'),
        ('Gestational','Gestational'),
        ('All','All'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    diabetes_type = models.CharField(max_length=20,choices=DIABETES_TYPES)
    takes_pills = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)


class UnitPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unit = models.CharField(max_length=10, choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L')])
    updated_at = models.DateTimeField(auto_now=True)



class ReligionPreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    religion = models.CharField(max_length=20, choices=[('Christian', 'Christian'), ('Moslem', 'Moslem')])
    updated_at = models.DateTimeField(auto_now=True)
class DevicePreference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    device = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now=True)
