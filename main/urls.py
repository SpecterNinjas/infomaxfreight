from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [

    # NAVBAR
    path('navbar/', NavbarListView.as_view(), name='navbar'),

    # Slider
    path('slider/', SliderListView.as_view(), name='slider'),

    # Services
    path('services/', ServicesListView.as_view(), name='services'),

    # Anons Bar
    path('anonsbar/', AnonsbarListView.as_view(), name='anonsbar'),

    # Section
    path('section/', SectionListView.as_view(), name='section'),

    # Carriers
    path('carriers/', CarriersListView.as_view(), name='carriers'),
    path('carriers-application-form/', CarriesApplicationListView.as_view(), name='carriers-application'),

    # Shippers

    # About Us
    path('about-us/', AboutUsListView.as_view(), name='about'),
    path('about-us-section/', AboutUsSectionListView.as_view(), name='about-us-section'),

    # Statistics
    path('statistics/', StatisticsListView.as_view(), name='statistics'),

    # Team
    path('team/', TeamListView.as_view(), name='team'),

    # Insights
    path('insights/', InsightsListView.as_view(), name='insights'),

    # Careers
    path('careers/', CareersListView.as_view(), name='careers'),

    # Vacancies
    path('vacancies/', VacanciesListView.as_view(), name='vacancies'),

    # Contact Us

    # Privacy-policy
    path('privacy-policy/', PrivacyPolicyListView.as_view(), name='privacy-policy'),

    # FAQ
    path('faq/', FAQListView.as_view(), name='faq'),

]
