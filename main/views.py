from django.shortcuts import render

from rest_framework import filters
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.pagination import PageNumberPagination
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


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 1000


class VacanciesListView(ListAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesSerializer
    pagination_class = StandardResultsSetPagination


class PrivacyPolicyListView(ListAPIView):
    queryset = PrivacyPolicy.objects.all()
    serializer_class = PrivacyPolicySerializer


class FAQListView(ListAPIView):
    queryset = FAQ.objects.filter(draft=False).order_by('-created')
    serializer_class = FAQSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['question', 'answer']


class FooterListView(ListAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer


class CarriersFormCreateAPI(CreateAPIView):
    serializer_class = CarriersFormSerializer


class ShippersFormCreateAPI(CreateAPIView):
    serializer_class = ShippersFormSerializer


class ContactUsCreateAPI(CreateAPIView):
    serializer_class = ContactUsSerializer


class RequestQuoteCreateAPI(CreateAPIView):
    serializer_class = RequestQuoteSerializer
