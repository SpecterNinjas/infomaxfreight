from rest_framework import serializers
from .models import *


class TruckTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckType
        fields = ['title', 'is_available']


class TruckLoadTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckloadType
        fields = ['title', 'is_available']


class CargoTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoType
        fields = ['title', 'is_available']


class CargoWeightSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoWeight
        fields = ['title', ]


class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = ['payment_type', ]


class WorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkType
        fields = ['work_type', ]


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


class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = '__all__'


class CarriersFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarriersForm
        fields = '__all__'


class ShippersFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippersForm
        fields = '__all__'


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'


class RequestQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestQuote
        fields = '__all__'
