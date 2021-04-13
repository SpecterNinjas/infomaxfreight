from django.shortcuts import render

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class NavbarListView(ListAPIView):
    queryset = Navbar.objects.all()
    serializer_class = NavbarSerializer


class SliderListView(ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class ServicesListView(ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class AnonsbarListView(ListAPIView):
    queryset = AnonsBar.objects.filter(is_active=True)
    serializer_class = AnonsBarSerializer


class SectionListView(ListAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer


class CarriersListView(ListAPIView):
    queryset = Carriers.objects.all()
    serializer_class = CarriersSerializer


class CarriesApplicationListView(ListAPIView):
    queryset = CarriesApplication.objects.all()
    serializer_class = CarriesApplicationSerializer


class AboutUsListView(ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class StatisticsListView(ListAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer


class AboutUsSectionListView(ListAPIView):
    queryset = AboutUsSection.objects.all()
    serializer_class = AboutUsSectionSerializer


class TeamListView(ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class InsightsListView(ListAPIView):
    queryset = Insights.objects.all()
    serializer_class = InsightsSerializer


class CareersListView(ListAPIView):
    queryset = Careers.objects.all()
    serializer_class = CareersSerializer


class VacanciesListView(ListAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesSerializer


class PrivacyPolicyListView(ListAPIView):
    queryset = PrivacyPolicy.objects.all()
    serializer_class = PrivacyPolicySerializer


class FAQListView(ListAPIView):
    queryset = FAQ.objects.filter(draft=False).order_by('-created')
    serializer_class = FAQSerializer
