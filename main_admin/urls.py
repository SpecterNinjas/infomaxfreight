from django.urls import path
from . import views

app_name = 'main_app'

urlpatterns = [
    path('', views.MainView.as_view(), name="main_page"),

    # NAVBAR
    path("navigation/", views.NavigationView.as_view(), name="navigation"),
    path("navigation_create/", views.NavigationCreateView.as_view(), name="navigation_create"),
    path("navigation/<int:pk>/", views.NavigationUpdateView.as_view(), name="navigation_update"),
    path("navigation_delete/<int:pk>/", views.NavigationDeleteView.as_view(), name="navigation_delete"),

    # SLIDER
    path("slider/", views.SliderView.as_view(), name="slider"),
    path("slider_create/", views.SliderCreateView.as_view(), name="slider_create"),
    path("slider/<int:pk>/", views.SliderUpdateView.as_view(), name="slider_update"),
    path("slider_delete/<int:pk>/", views.SliderDeleteView.as_view(), name="slider_delete"),

    # SERVICE
    path("service/", views.ServiceView.as_view(), name="service"),
    path("service_create/", views.ServiceCreateView.as_view(), name="service_create"),
    path("service/<int:pk>/", views.ServiceUpdateView.as_view(), name="service_update"),
    path("service_delete/<int:pk>/", views.ServiceDeleteView.as_view(), name="service_delete"),

    # Anons Bar
    path("anonsbar/", views.AnonsBarView.as_view(), name="anons_bar"),
    path("anonsbar_create/", views.AnonsBarCreateView.as_view(), name="anonsbar_create"),
    path("anonsbar/<int:pk>/", views.AnonsBarUpdateView.as_view(), name="anonsbar_update"),
    path("anonsbar_delete/<int:pk>/", views.AnonsBarDeleteView.as_view(), name="anonsbar_delete"),

    # Section
    path("section/", views.SectionView.as_view(), name="section"),
    path("section_create/", views.SectionCreateView.as_view(), name="section_create"),
    path("section/<int:pk>/", views.SectionUpdateView.as_view(), name="section_update"),
    path("section_delete/<int:pk>/", views.SectionDeleteView.as_view(), name="section_delete"),

    # Carriers
    path("carriers/", views.CarrierView.as_view(), name="carriers"),
    path("carriers_create/", views.CarrierCreateView.as_view(), name="carriers_create"),
    path("carriers/<int:pk>/", views.CarrierUpdateView.as_view(), name="carriers_update"),
    path("carriers_delete/<int:pk>/", views.CarrierDeleteView.as_view(), name="carriers_delete"),

    # Carriers Application
    path("carriers_app/", views.CarriersAppView.as_view(), name="carriers_app"),
    path("carriers_app_create/", views.CarrierAppCreateView.as_view(), name="carriers_create"),
    path("carriers_app/<int:pk>/", views.CarrierAppUpdateView.as_view(), name="carriers_update"),
    path("carriers_app_delete/<int:pk>/", views.CarrierAppDeleteView.as_view(), name="carriers_delete"),

    # Truckload Type
    path("truckload_type/", views.TruckloadTypeView.as_view(), name="truckload_type"),
    path("truckload_type_create/", views.TruckloadTypeCreateView.as_view(), name="truckload_type_create"),
    path("truckload_type/<int:pk>/", views.TruckloadTypeUpdateView.as_view(), name="truckload_type_update"),
    path("truckload_type_delete/<int:pk>/", views.TruckloadTypeDeleteView.as_view(), name="truckload_type_delete"),

    # Truck Type
    path("truck_type/", views.TruckTypeView.as_view(), name="truck_type"),
    path("truck_type_create/", views.TruckTypeCreateView.as_view(), name="truck_type_create"),
    path("truck_type/<int:pk>/", views.TruckTypeUpdateView.as_view(), name="truck_type_update"),
    path("truck_type_delete/<int:pk>/", views.TruckTypeDeleteView.as_view(), name="truck_type_delete"),

    # Cargo Type
    path("cargo_type/", views.CargoTypeView.as_view(), name="cargo_type"),
    path("cargo_type_create/", views.CargoTypeCreateView.as_view(), name="cargo_type_create"),
    path("cargo_type/<int:pk>/", views.CargoTypeUpdateView.as_view(), name="cargo_type_update"),
    path("cargo_type_delete/<int:pk>/", views.CargoTypeDeleteView.as_view(), name="cargo_type_delete"),

    # Cargo Weight
    path("cargo_weight/", views.CargoWeightView.as_view(), name="cargo_weight"),
    path("cargo_weight_create/", views.CargoWeightCreateView.as_view(), name="cargo_weight_create"),
    path("cargo_weight/<int:pk>/", views.CargoWeightUpdateView.as_view(), name="cargo_weight_update"),
    path("cargo_weight_delete/<int:pk>/", views.CargoWeightDeleteView.as_view(), name="cargo_weight_delete"),

    # Shipper Form
    path("shipper_form/", views.ShipperFormView.as_view(), name="shipper_form"),
    path("shipper_form_create/", views.ShipperFormCreateView.as_view(), name="shipper_form_create"),
    path("shipper_form/<int:pk>/", views.ShipperFormUpdateView.as_view(), name="shipper_form_update"),
    path("shipper_form_delete/<int:pk>/", views.ShipperFormDeleteView.as_view(), name="shipper_form_delete"),

    # About Us
    path("about_us/", views.AboutUsView.as_view(), name="about_us"),
    path("about_us_create/", views.AboutUsCreateView.as_view(), name="about_us_create"),
    path("about_us/<int:pk>/", views.AboutUsUpdateView.as_view(), name="about_us_update"),
    path("about_us_delete/<int:pk>/", views.AboutUsDeleteView.as_view(), name="about_us_delete"),

    # Statistics
    path("statistics/", views.StatisticsView.as_view(), name="statistics"),
    path("statistics_create/", views.StatisticsCreateView.as_view(), name="statistics_create"),
    path("statistics/<int:pk>/", views.StatisticsUpdateView.as_view(), name="statistics_update"),
    path("statistics_delete/<int:pk>/", views.StatisticsDeleteView.as_view(), name="statistics_delete"),

    # About Us Section
    path("about_section/", views.AboutUsSectionView.as_view(), name="about_section"),
    path("about_section_create/", views.AboutUsSectionCreateView.as_view(), name="about_section_create"),
    path("about_section/<int:pk>/", views.AboutUsSectionUpdateView.as_view(), name="about_section_update"),
    path("about_section_delete/<int:pk>/", views.AboutUsSectionDeleteView.as_view(), name="about_section_delete"),

    # TEAM
    path("team/", views.TeamView.as_view(), name="team"),
    path("team_create/", views.TeamCreateView.as_view(), name="team_create"),
    path("team/<int:pk>/", views.TeamUpdateView.as_view(), name="team_update"),
    path("team_delete/<int:pk>/", views.TeamDeleteView.as_view(), name="team_delete"),

    # Insights
    path("insight/", views.InsightView.as_view(), name="insight"),
    path("insight_create/", views.InsightCreateView.as_view(), name="insight_create"),
    path("insight/<int:pk>/", views.InsightUpdateView.as_view(), name="insight_update"),
    path("insight_delete/<int:pk>/", views.InsightDeleteView.as_view(), name="insight_delete"),

    # Careers
    path("career/", views.CareerView.as_view(), name="career"),
    path("career_create/", views.CareerCreateView.as_view(), name="career_create"),
    path("career/<int:pk>/", views.CareerUpdateView.as_view(), name="career_update"),
    path("career_delete/<int:pk>/", views.CareerDeleteView.as_view(), name="career_delete"),

    # Payment Types
    path("payment_type/", views.PaymentTypeView.as_view(), name="payment_type"),
    path("payment_type_create/", views.PaymentTypeCreateView.as_view(), name="payment_type_create"),
    path("payment_type/<int:pk>/", views.PaymentTypeUpdateView.as_view(), name="payment_type_update"),
    path("payment_type_delete/<int:pk>/", views.PaymentTypeDeleteView.as_view(), name="payment_type_delete"),

    # Work Types
    path("work_type/", views.WorkTypeView.as_view(), name="work_type"),
    path("work_type_create/", views.WorkTypeCreateView.as_view(), name="work_type_create"),
    path("work_type/<int:pk>/", views.WorkTypeUpdateView.as_view(), name="work_type_update"),
    path("work_type_delete/<int:pk>/", views.WorkTypeDeleteView.as_view(), name="work_type_delete"),

    # Vacancies
    path("vacancy/", views.VacancyView.as_view(), name="vacancy"),
    path("vacancy_create/", views.VacancyCreateView.as_view(), name="vacancy_create"),
    path("vacancy/<int:pk>/", views.VacancyUpdateView.as_view(), name="vacancy_update"),
    path("vacancy_delete/<int:pk>/", views.VacancyDeleteView.as_view(), name="vacancy_delete"),

    # Contact Us
    path("contact/", views.ContactUsView.as_view(), name="contact"),
    path("contact/<int:pk>/", views.ContactUsUpdateView.as_view(), name="contact_update"),
    path("contact_delete/<int:pk>/", views.ContactUsDeleteView.as_view(), name="contact_delete"),

    # Privacy Policy
    path("privacy/", views.PrivacyPolicyView.as_view(), name="privacy"),
    path("privacy_create/", views.PrivacyPolicyCreateView.as_view(), name="privacy_create"),
    path("privacy/<int:pk>/", views.PrivacyPolicyUpdateView.as_view(), name="privacy_update"),
    path("privacy_delete/<int:pk>/", views.PrivacyPolicyDeleteView.as_view(), name="privacy_delete"),

    # FAQ
    path("faq/", views.FAQView.as_view(), name="faq"),
    path("faq_create/", views.FAQCreateView.as_view(), name="faq_create"),
    path("faq/<int:pk>/", views.FAQUpdateView.as_view(), name="faq_update"),
    path("faq_delete/<int:pk>/", views.FAQDeleteView.as_view(), name="faq_delete"),

    # Footer
    path("footer/", views.FooterView.as_view(), name="footer"),
    path("footer/<int:pk>/", views.FooterUpdateView.as_view(), name="footer_update"),
    path("footer_delete/<int:pk>/", views.FooterDeleteView.as_view(), name="footer_delete"),

    # Quote
    path("quote/", views.RequestQuoteView.as_view(), name="quote"),
    path("quote_create/", views.RequestQuoteCreateView.as_view(), name="quote_create"),
    path("quote/<int:pk>/", views.RequestQuoteUpdateView.as_view(), name="quote_update"),
    path("quote_delete/<int:pk>/", views.RequestQuoteDeleteView.as_view(), name="quote_delete"),

    # Carriers Form
    path("carriers_form/", views.CarriersFormView.as_view(), name="carriers_form"),
    path("carriers_form_create/", views.CarriersFormCreateView.as_view(), name="carriers_form_create"),
    path("carriers_form/<int:pk>/", views.CarriersFormUpdateView.as_view(), name="carriers_form_update"),
    path("carriers_form_delete/<int:pk>/", views.CarriersFormDeleteView.as_view(), name="carriers_form_delete"),

]
