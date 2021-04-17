from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [

    # Truck Type
    path('truck_type/', TruckTypeListView.as_view(), name='truck_type'),

    # TruckLoad Type
    path('truckload_type/', TruckloadTypeListView.as_view(), name='truckload_type'),

    # Cargo Type
    path('cargo_type/', CargoTypeListView.as_view(), name='cargo_type'),

    # Cargo Weight
    path('cargo_weight/', CargoWeightListView.as_view(), name='cargo_weight'),

    # payment Type
    path('payment_type/', PaymentTypeListView.as_view(), name='payment_type'),

    # work Type
    path('work_type/', WorkTypeListView.as_view(), name='work_type'),


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
    path('carriers-application-form-link/', CarriesApplicationListView.as_view(), name='carriers-application'),
    path('carriers-form/', CarriersFormCreateAPI.as_view(), name='carriers-form'),

    # Shippers
    path('shippers/', ShippersFormCreateAPI.as_view(), name='shippers'),

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
    path('contact/', ContactUsCreateAPI.as_view(), name='contact'),

    # Privacy-policy
    path('privacy-policy/', PrivacyPolicyListView.as_view(), name='privacy-policy'),

    # FAQ
    path('faq/', FAQListView.as_view(), name='faq'),

    # Footer
    path('footer/', FooterListView.as_view(), name='footer'),

    # Quote
    path('quote/', RequestQuoteCreateAPI.as_view(), name='quote'),

]
