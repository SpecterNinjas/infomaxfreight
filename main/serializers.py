from rest_framework import serializers
from .models import *


class NavbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navbar
        fields = ['title', 'order', 'url']


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['title', 'description', 'image', 'url']


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class AnonsBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnonsBar
        fields = ['description', 'image', 'url']


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'


class CarriersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carriers
        fields = '__all__'


class CarriesApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarriesApplication
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'


class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = '__all__'


class AboutUsSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsSection
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class InsightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insights
        fields = '__all__'


class CareersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Careers
        fields = '__all__'


class VacanciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = '__all__'


class PrivacyPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']
