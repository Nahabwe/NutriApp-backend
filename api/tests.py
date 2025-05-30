from django.test import TestCase
from django.contrib.auth.models import User
from .models import DiabetesProfile, HealthMetric, FoodItem, HealthTip, Recipe
from datetime import date, timedelta
from django.core.exceptions import ValidationError

# -------------------------------
# DiabetesProfile Tests
# -------------------------------
class DiabetesProfileTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_create_valid_diabetes_profile(self):
        profile = DiabetesProfile.objects.create(
            user=self.user,
            age=30,
            gender='Male',
            diabet_type='Type 1',
            diagnosis_date=date(2022, 1, 1)
        )
        self.assertEqual(profile.age, 30)
        self.assertEqual(str(profile), 'testuser')

    def test_invalid_age(self):
        profile = DiabetesProfile(
            user=self.user,
            age=-1,
            gender='Male',
            diabet_type='Type 2',
            diagnosis_date=date(2022, 1, 1)
        )
        with self.assertRaises(ValidationError):
            profile.clean()

    def test_future_diagnosis_date(self):
        future_date = date.today() + timedelta(days=1)
        profile = DiabetesProfile(
            user=self.user,
            age=25,
            gender='Female',
            diabet_type='Type 1',
            diagnosis_date=future_date
        )
        with self.assertRaises(ValidationError):
            profile.clean()

# -------------------------------
# HealthMetric Tests
# -------------------------------
class HealthMetricTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='metricuser', password='testpass')
        self.profile = DiabetesProfile.objects.create(
            user=self.user,
            age=35,
            gender='Female',
            diabet_type='Type 2',
            diagnosis_date=date(2021, 6, 15)
        )

    def test_valid_health_metric(self):
        metric = HealthMetric.objects.create(
            profile=self.profile,
            fasting_glucose='90',
            hba1c='5.5',
            daily_carbs='120',
            weight='70',
            height='170',
            bmi='24.5'
        )
        self.assertEqual(str(metric), 'Metrics for metricuser')

    def test_invalid_bmi_value(self):
        metric = HealthMetric(
            profile=self.profile,
            fasting_glucose='95',
            hba1c='6.0',
            daily_carbs='150',
            weight='80',
            height='180',
            bmi='100'  # Invalid BMI
        )
        with self.assertRaises(ValidationError):
            metric.clean()

    def test_non_numeric_bmi(self):
        metric = HealthMetric(
            profile=self.profile,
            fasting_glucose='95',
            hba1c='6.0',
            daily_carbs='150',
            weight='80',
            height='180',
            bmi='invalid'  # Not a number
        )
        with self.assertRaises(ValidationError):
            metric.clean()

# -------------------------------
# FoodItem Tests
# -------------------------------
class FoodItemTests(TestCase):
    def test_create_food_item(self):
        food = FoodItem.objects.create(
            title='Chicken Salad',
            image_url='http://example.com/image.jpg',
            recipe='Mix and serve'
        )
        self.assertEqual(str(food), 'Chicken Salad')

# -------------------------------
# HealthTip Tests
# -------------------------------
class HealthTipTests(TestCase):
    def test_create_health_tip(self):
        tip = HealthTip.objects.create(
            title='Stay Active',
            body='Walk 30 minutes a day',
            nutritionist='Dr. Sam',
            image_url='http://example.com/tip.jpg'
        )
        self.assertEqual(str(tip), 'Stay Active')

# -------------------------------
# Recipe Tests
# -------------------------------
class RecipeTests(TestCase):
    def test_create_recipe(self):
        recipe = Recipe.objects.create(
            name='Oatmeal Breakfast',
            video='http://example.com/video.mp4',
            description='Healthy oatmeal recipe',
            suitable_for='Type 1',
            category='Breakfast',
            calories=300,
            carbs='50g'
        )
        self.assertEqual(str(recipe), 'Oatmeal Breakfast')
