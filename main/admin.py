from django.contrib import admin
from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget


class CarriersAdminCKEditorForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Carriers
        fields = '__all__'


class AboutUsAdminCKEditorForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = AboutUs
        fields = '__all__'


class AboutUsSectionAdminCKEditorForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = AboutUsSection
        fields = '__all__'


class VacanciesAdminCKEditorForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Vacancies
        fields = '__all__'


class CareersAdminCKEditorForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Careers
        fields = '__all__'


class InsightsAdminCKEditorForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Insights
        fields = '__all__'


class FAQAdminCKEditorForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Insights
        fields = '__all__'


class PrivacyPolicyAdminCKEditorForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = PrivacyPolicy
        fields = '__all__'


@admin.register(Navbar)
class NavbarAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'url']


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'url', 'draft']


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'url']


@admin.register(AnonsBar)
class AnonsBarAdmin(admin.ModelAdmin):
    list_display = ['description', 'image', 'is_active', 'url']


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'icon']


@admin.register(Carriers)
class CarriersAdmin(admin.ModelAdmin):
    form = CarriersAdminCKEditorForm
    list_display = ['title', 'image']


@admin.register(CarriesApplication)
class CarriesApplication(admin.ModelAdmin):
    list_display = ['description', 'image', 'url']


@admin.register(TruckloadType)
class TruckloadTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_available']


@admin.register(TruckType)
class TruckTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_available']


@admin.register(CargoType)
class CargoTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_available']


@admin.register(CargoWeight)
class CargoWeightAdmin(admin.ModelAdmin):
    list_display = ['title', ]


# @admin.register(CarriersForm)
# class CarriersFormAdmin(admin.ModelAdmin):
#     list_display = ['fullname', 'company', 'pickup_date', 'delivery_date', 'from_city',
#                     'to_city']


@admin.register(ShippersForm)
class ShippersFormAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'company', 'pickup_date', 'delivery_date', 'from_city',
                    'to_city']


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    form = AboutUsAdminCKEditorForm
    list_display = ['title', 'image']


@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ['title', 'quantity', 'image']


@admin.register(AboutUsSection)
class AboutUsSectionAdmin(admin.ModelAdmin):
    form = AboutUsSectionAdminCKEditorForm
    list_display = ['title', 'image']


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'job_title', 'image']


@admin.register(Insights)
class InsightsAdmin(admin.ModelAdmin):
    form = InsightsAdminCKEditorForm
    list_display = ['title', 'image']


@admin.register(Careers)
class CareersAdmin(admin.ModelAdmin):
    form = CareersAdminCKEditorForm
    list_display = ['title', ]


@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ['payment_type', ]


@admin.register(WorkType)
class WorkTypeAdmin(admin.ModelAdmin):
    list_display = ['work_type', ]


@admin.register(Vacancies)
class VacanciesAdmin(admin.ModelAdmin):
    form = VacanciesAdminCKEditorForm
    list_display = ['job_title', 'company', 'work_type', 'payment_type', 'work_hour', 'quantity']


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'email', 'phone', 'message']


@admin.register(RequestQuote)
class RequestQuoteAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'company', 'pickup_date', 'delivery_date', 'from_city',
                    'to_city']


# admin.site.register(PrivacyPolicy)

@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    form = PrivacyPolicyAdminCKEditorForm
    list_display = ['pk', 'created', 'updated']


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    form = FAQAdminCKEditorForm
    list_display = ['question', 'created', 'updated', 'draft']


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ['phone', 'fax', 'mail', 'short_address']


@admin.register(CarriersForm)
class CarriersFormAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'company', 'pickup_date', 'delivery_date', 'from_city', 'to_city', 'phone', 'email']
