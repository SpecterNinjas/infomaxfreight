from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView
from rest_framework.reverse import reverse

from main.models import *
from .forms import *


class MainView(ListView):
    queryset = Navbar.objects.all()
    template_name = 'admin_info/main/index.html'


""" Navigation Part """


class NavigationView(ListView):
    template_name = 'admin_info/navigation/index.html'
    context_object_name = 'navigation_list'
    queryset = Navbar.objects.all()


class NavigationCreateView(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/navigation/create.html')

    def post(self, request):
        print(request.POST)
        form = NavigationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:navigation')
        else:
            return render(request, 'admin_info/navigation/create.html', {'form': form})


class NavigationUpdateView(UpdateView):
    model = Navbar
    template_name = "admin_info/navigation/update.html"
    context_object_name = 'navigation'
    form_class = NavigationForm
    success_url = reverse_lazy("main_app:navigation")


class NavigationDeleteView(DeleteView):
    model = Navbar
    success_url = reverse_lazy("main_app:navigation")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


""" End Navigation Part """


class SliderView(ListView):
    template_name = 'admin_info/slider/index.html'
    context_object_name = 'slider_list'
    queryset = Slider.objects.all()


class SliderUpdateView(UpdateView):
    model = Slider
    template_name = "admin_info/slider/update.html"
    context_object_name = 'slider'
    form_class = SliderForm
    success_url = reverse_lazy("main_app:slider")


class SliderDeleteView(DeleteView):
    model = Slider
    success_url = reverse_lazy("main_app:slider")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class SliderCreateView(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/slider/create.html')

    def post(self, request):
        print(request.POST)
        form = SliderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:slider')
        else:
            return render(request, 'admin_info/slider/create.html', {'form': form})


class ServiceView(ListView):
    template_name = 'admin_info/services/index.html'
    context_object_name = 'service_list'
    queryset = Services.objects.all()


class ServiceDeleteView(DeleteView):
    model = Services
    success_url = reverse_lazy("main_app:service")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ServiceCreateView(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/services/create.html')

    def post(self, request):
        print(request.POST)
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:service')
        else:
            return render(request, 'admin_info/services/create.html', {'form': form})


class ServiceUpdateView(UpdateView):
    model = Services
    template_name = "admin_info/services/update.html"
    context_object_name = 'service'
    form_class = ServiceForm
    success_url = reverse_lazy("main_app:service")


class AnonsBarView(ListView):
    template_name = 'admin_info/anonsbar/index.html'
    context_object_name = 'anons_list'
    queryset = AnonsBar.objects.all()


class AnonsBarCreateView(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/anonsbar/create.html')

    def post(self, request):
        form = AnonsBarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:anons_bar')
        else:
            return render(request, 'admin_info/anonsbar/create.html', {'form': form})


class AnonsBarUpdateView(UpdateView):
    model = AnonsBar
    template_name = "admin_info/anonsbar/update.html"
    context_object_name = 'anonsbar'
    form_class = AnonsBarForm
    success_url = reverse_lazy("main_app:anons_bar")


class AnonsBarDeleteView(DeleteView):
    model = AnonsBar
    success_url = reverse_lazy("main_app:anons_bar")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class SectionView(ListView):
    template_name = 'admin_info/section/index.html'
    context_object_name = 'section_list'
    queryset = Section.objects.all()


class SectionCreateView(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/section/create.html')

    def post(self, request):
        form = SectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:section')
        else:
            return render(request, 'admin_info/section/create.html', {'form': form})


class SectionDeleteView(DeleteView):
    model = Section
    success_url = reverse_lazy("main_app:section")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class SectionUpdateView(UpdateView):
    model = Section
    template_name = "admin_info/section/update.html"
    context_object_name = 'section'
    form_class = SectionForm
    success_url = reverse_lazy("main_app:section")


class CarrierView(ListView):
    template_name = 'admin_info/carriers/index.html'
    context_object_name = 'carriers'
    queryset = Carriers.objects.all()


class CarrierCreateView(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/carriers/create.html')

    def post(self, request):
        form = CarrierForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:carriers')
        else:
            return render(request, 'admin_info/carriers/create.html', {'form': form})


class CarrierUpdateView(UpdateView):
    model = Carriers
    template_name = "admin_info/carriers/update.html"
    context_object_name = 'carrier'
    form_class = CarrierForm
    success_url = reverse_lazy("main_app:carriers")


class CarrierDeleteView(DeleteView):
    model = Carriers
    success_url = reverse_lazy("main_app:carriers")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class CarriersAppView(ListView):
    template_name = 'admin_info/carriers_application/index.html'
    context_object_name = 'carriers_app'
    queryset = CarriesApplication.objects.all()


class CarrierAppCreateView(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/carriers_application/create.html')

    def post(self, request):
        form = CarrierAppForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:carriers_app')
        else:
            return render(request, 'admin_info/carriers_application/create.html', {'form': form})


class CarrierAppUpdateView(UpdateView):
    model = CarriesApplication
    template_name = "admin_info/carriers_application/update.html"
    context_object_name = 'carrier_app'
    form_class = CarrierAppForm
    success_url = reverse_lazy("main_app:carriers_app")


class CarrierAppDeleteView(DeleteView):
    model = CarriesApplication
    success_url = reverse_lazy("main_app:carriers_app")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class TruckloadTypeView(ListView):
    template_name = 'admin_info/truckload_type/index.html'
    context_object_name = 'truckload_types'
    queryset = TruckloadType.objects.all()


class TruckloadTypeCreateView(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/truckload_type/create.html')

    def post(self, request):
        form = TruckloadTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:truckload_type')
        else:
            return render(request, 'admin_info/truckload_type/create.html', {'form': form})


class TruckloadTypeUpdateView(UpdateView):
    model = TruckloadType
    template_name = "admin_info/truckload_type/update.html"
    context_object_name = 'truckload_type'
    form_class = TruckloadTypeForm
    success_url = reverse_lazy("main_app:truckload_type")


class TruckloadTypeDeleteView(DeleteView):
    model = TruckloadType
    success_url = reverse_lazy("main_app:truckload_type")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class TruckTypeView(ListView):
    template_name = 'admin_info/truck_type/index.html'
    context_object_name = 'truckload_types'
    queryset = TruckType.objects.all()


class TruckTypeCreateView(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/truck_type/create.html')

    def post(self, request):
        form = TruckTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:truck_type')
        else:
            return render(request, 'admin_info/truck_type/create.html', {'form': form})


class TruckTypeUpdateView(UpdateView):
    model = TruckType
    template_name = "admin_info/truck_type/update.html"
    context_object_name = 'truck_type'
    form_class = TruckTypeForm
    success_url = reverse_lazy("main_app:truck_type")


class TruckTypeDeleteView(DeleteView):
    model = TruckType
    success_url = reverse_lazy("main_app:truck_type")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class CargoTypeView(ListView):
    template_name = 'admin_info/cargo_type/index.html'
    context_object_name = 'cargo_types'
    queryset = CargoType.objects.all()


class CargoTypeCreateView(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/cargo_type/create.html')

    def post(self, request):
        form = CargoTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:cargo_type')
        else:
            return render(request, 'admin_info/cargo_type/create.html', {'form': form})


class CargoTypeUpdateView(UpdateView):
    model = CargoType
    template_name = "admin_info/cargo_type/update.html"
    context_object_name = 'cargo_type'
    form_class = CargoTypeForm
    success_url = reverse_lazy("main_app:cargo_type")


class CargoTypeDeleteView(DeleteView):
    model = CargoType
    success_url = reverse_lazy("main_app:cargo_type")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class CargoWeightView(ListView):
    template_name = 'admin_info/cargo_weight/index.html'
    context_object_name = 'cargo_weights'
    queryset = CargoWeight.objects.all()


class CargoWeightCreateView(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/cargo_weight/create.html')

    def post(self, request):
        form = CargoWeightForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:cargo_weight')
        else:
            return render(request, 'admin_info/cargo_weight/create.html', {'form': form})


class CargoWeightUpdateView(UpdateView):
    model = CargoWeight
    template_name = "admin_info/cargo_weight/update.html"
    context_object_name = 'cargo_weight'
    form_class = CargoTypeForm
    success_url = reverse_lazy("main_app:cargo_weight")


class CargoWeightDeleteView(DeleteView):
    model = CargoWeight
    success_url = reverse_lazy("main_app:cargo_weight")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ShipperFormDeleteView(DeleteView):
    model = ShippersForm
    success_url = reverse_lazy("main_app:shipper_form")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ShipperFormView(ListView):
    template_name = 'admin_info/shipper_form/index.html'
    context_object_name = 'shipper_form'
    queryset = ShippersForm.objects.all()


class ShipperFormUpdateView(UpdateView):
    model = ShippersForm
    template_name = "admin_info/shipper_form/update.html"
    context_object_name = 'shipper_form'
    form_class = ShippersShowForm
    success_url = reverse_lazy("main_app:shipper_form")

    def get_context_data(self, **kwargs):
        truckLoadTypes = TruckloadType.objects.all()
        truck_types = TruckType.objects.all()
        cargo_types = CargoType.objects.all()
        cargo_weight = CargoWeight.objects.all()

        context = super(ShipperFormUpdateView, self).get_context_data(**kwargs)
        context['truckload_types'] = truckLoadTypes
        context['f2'] = truck_types
        context['f3'] = cargo_types
        context['f4'] = cargo_weight
        return context

    # def form_invalid(self, form):
    #     print(form)
    #     response = super().form_invalid(form)
    #     if self.request.accepts('text/html'):
    #         return response
    #     else:
    #         return JsonResponse(form.errors, status=400)
    #
    #
    # def form_valid(self, form):
    #     print(form.instance.truck_type , 'rad0')
    #     return super(ShipperFormUpdateView, self).form_valid(form)


class AboutUsView(ListView):
    template_name = 'admin_info/about_us/index.html'
    context_object_name = 'abouts'
    queryset = AboutUs.objects.all()


class AboutUsCreateView(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/about_us/create.html')

    def post(self, request):
        form = AboutUsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:about_us')
        else:
            return render(request, 'admin_info/about_us/create.html', {'form': form})


class AboutUsUpdateView(UpdateView):
    model = AboutUs
    template_name = "admin_info/about_us/update.html"
    context_object_name = 'about'
    form_class = AboutUsForm
    success_url = reverse_lazy("main_app:about_us")


class AboutUsDeleteView(DeleteView):
    model = AboutUs
    success_url = reverse_lazy("main_app:about_us")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class StatisticsView(ListView):
    template_name = 'admin_info/statistics/index.html'
    context_object_name = 'statistics'
    queryset = Statistics.objects.all()


class StatisticsCreateView(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/statistics/create.html')

    def post(self, request):
        form = StatisticsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:statistics')
        else:
            return render(request, 'admin_info/statistics/create.html', {'form': form})


class StatisticsUpdateView(UpdateView):
    model = Statistics
    template_name = "admin_info/statistics/update.html"
    context_object_name = 'statistics'
    form_class = StatisticsForm
    success_url = reverse_lazy("main_app:statistics")


class StatisticsDeleteView(DeleteView):
    model = Statistics
    success_url = reverse_lazy("main_app:statistics")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class AboutUsSectionView(ListView):
    template_name = 'admin_info/about_us_section/index.html'
    context_object_name = 'abouts'
    queryset = AboutUsSection.objects.all()


class AboutUsSectionCreateView(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/about_us_section/create.html')

    def post(self, request):
        form = AboutUsSectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:about_section')
        else:
            return render(request, 'admin_info/about_us_section/create.html', {'form': form})


class AboutUsSectionUpdateView(UpdateView):
    model = AboutUsSection
    template_name = "admin_info/about_us_section/update.html"
    context_object_name = 'about'
    form_class = AboutUsSectionForm
    success_url = reverse_lazy("main_app:about_section")


class AboutUsSectionDeleteView(DeleteView):
    model = AboutUsSection
    success_url = reverse_lazy("main_app:about_section")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class TeamView(ListView):
    template_name = 'admin_info/team/index.html'
    context_object_name = 'team'
    queryset = Team.objects.all()


class TeamCreateView(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/team/create.html')

    def post(self, request):
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:team')
        else:
            return render(request, 'admin_info/team/create.html', {'form': form})


class TeamUpdateView(UpdateView):
    model = Team
    template_name = "admin_info/team/update.html"
    context_object_name = 'member'
    form_class = TeamForm
    success_url = reverse_lazy("main_app:team")


class TeamDeleteView(DeleteView):
    model = Team
    success_url = reverse_lazy("main_app:team")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class InsightView(ListView):
    template_name = 'admin_info/insights/index.html'
    context_object_name = 'insight'
    queryset = Insights.objects.all()


class InsightCreateView(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/insights/create.html')

    def post(self, request):
        form = InsightForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:insight')
        else:
            return render(request, 'admin_info/insights/create.html', {'form': form})


class InsightUpdateView(UpdateView):
    model = Insights
    template_name = "admin_info/insights/update.html"
    context_object_name = 'about'
    form_class = InsightForm
    success_url = reverse_lazy("main_app:insight")


class InsightDeleteView(DeleteView):
    model = Insights
    success_url = reverse_lazy("main_app:insight")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class CareerView(ListView):
    template_name = 'admin_info/careers/index.html'
    context_object_name = 'careers'
    queryset = Careers.objects.all()


class CareerCreateView(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/careers/create.html')

    def post(self, request):
        form = CareerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:career')
        else:
            return render(request, 'admin_info/careers/create.html', {'form': form})


class CareerUpdateView(UpdateView):
    model = Careers
    template_name = "admin_info/careers/update.html"
    context_object_name = 'career'
    form_class = CareerForm
    success_url = reverse_lazy("main_app:career")


class CareerDeleteView(DeleteView):
    model = Careers
    success_url = reverse_lazy("main_app:career")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class PaymentTypeCreateView(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/payment_type/create.html')

    def post(self, request):
        form = PaymentTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:payment_type')
        else:
            return render(request, 'admin_info/payment_type/create.html', {'form': form})


class PaymentTypeView(ListView):
    template_name = 'admin_info/payment_type/index.html'
    context_object_name = 'cargo_weights'
    queryset = PaymentType.objects.all()


class PaymentTypeUpdateView(UpdateView):
    model = PaymentType
    template_name = "admin_info/payment_type/update.html"
    context_object_name = 'payment_type'
    form_class = PaymentTypeForm
    success_url = reverse_lazy("main_app:payment_type")


class PaymentTypeDeleteView(DeleteView):
    model = PaymentType
    success_url = reverse_lazy("main_app:payment_type")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class WorkTypeView(ListView):
    template_name = 'admin_info/work_type/index.html'
    context_object_name = 'work_types'
    queryset = WorkType.objects.all()


class ShipperFormCreateView(ListView):

    def get(self, request, *args, **kwargs):
        truckload_types = TruckloadType.objects.all()
        truck_types = TruckType.objects.all()
        cargo_types = CargoType.objects.all()
        cargo_weight = CargoWeight.objects.all()

        return render(request, 'admin_info/shipper_form/create.html', {'f1': truckload_types, 'f2': truck_types,
                                                                       'f3': cargo_types, 'f4': cargo_weight})

    def post(self, request):
        form = ShippersShowForm(request.POST, request.FILES)
        truckload_types = TruckloadType.objects.all()
        truck_types = TruckType.objects.all()
        cargo_types = CargoType.objects.all()
        cargo_weight = CargoWeight.objects.all()
        if form.is_valid():
            form.save()
            return redirect('main_app:shipper_form')
        else:
            return render(request, 'admin_info/shipper_form/create.html',
                          {'form': form, 'f1': truckload_types, 'f2': truck_types,
                           'f3': cargo_types, 'f4': cargo_weight})


class VacancyCreateView(ListView):

    def get(self, request, *args, **kwargs):
        work_type = WorkType.objects.all()
        payment_type = PaymentType.objects.all()
        return render(request, 'admin_info/vacancies/create.html', {'f1': work_type, 'f2': payment_type})

    def post(self, request):
        work_type = WorkType.objects.all()
        payment_type = PaymentType.objects.all()
        form = WorkTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:work_type')
        else:
            return render(request, 'admin_info/work_type/create.html',
                          {'form': form, 'f1': work_type, 'f2': payment_type})


class WorkTypeCreateView(ListView):

    def get(self, request, *args, **kwargs):
        work_type = WorkType.objects.all()
        payment_type = PaymentType.objects.all()
        return render(request, 'admin_info/work_type/create.html', {'f1': work_type, 'f2': payment_type})

    def post(self, request):
        work_type = WorkType.objects.all()
        payment_type = PaymentType.objects.all()
        form = WorkTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:work_type')
        else:
            return render(request, 'admin_info/work_type/create.html',
                          {'form': form, 'f1': work_type, 'f2': payment_type})


class WorkTypeUpdateView(UpdateView):
    model = WorkType
    template_name = "admin_info/work_type/update.html"
    context_object_name = 'work_type'
    form_class = WorkTypeForm
    success_url = reverse_lazy("main_app:work_type")


class WorkTypeDeleteView(DeleteView):
    model = WorkType
    success_url = reverse_lazy("main_app:work_type")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class VacancyView(ListView):
    template_name = 'admin_info/vacancies/index.html'
    context_object_name = 'vacancies'
    queryset = Vacancies.objects.all()


class ContactUsView(ListView):
    template_name = 'admin_info/contact/index.html'
    context_object_name = 'contacts'
    queryset = ContactUs.objects.all()


class ContactUsUpdateView(UpdateView):
    model = ContactUs
    template_name = "admin_info/contact/update.html"
    context_object_name = 'contact'
    form_class = ContactForm
    success_url = reverse_lazy("main_app:contact")


class ContactUsDeleteView(DeleteView):
    model = ContactUs
    success_url = reverse_lazy("main_app:contact")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class PrivacyPolicyView(ListView):
    template_name = 'admin_info/privacy/index.html'
    context_object_name = 'policies'
    queryset = PrivacyPolicy.objects.all()


class PrivacyPolicyCreateView(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/privacy/create.html')

    def post(self, request):
        form = PrivacyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:privacy')
        else:
            return render(request, 'admin_info/privacy/create.html', {'form': form})


class PrivacyPolicyUpdateView(UpdateView):
    model = PrivacyPolicy
    template_name = "admin_info/privacy/update.html"
    context_object_name = 'privacy'
    form_class = PrivacyForm
    success_url = reverse_lazy("main_app:privacy")


class PrivacyPolicyDeleteView(DeleteView):
    model = PrivacyPolicy
    success_url = reverse_lazy("main_app:privacy")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class FAQView(ListView):
    template_name = 'admin_info/faq/index.html'
    context_object_name = 'faqs'
    queryset = FAQ.objects.all()


class FAQCreateView(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/faq/create.html')

    def post(self, request):
        form = FAQForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:faq')
        else:
            return render(request, 'admin_info/faq/create.html', {'form': form})


class FAQUpdateView(UpdateView):
    model = FAQ
    template_name = "admin_info/faq/update.html"
    context_object_name = 'faq'
    form_class = FAQForm
    success_url = reverse_lazy("main_app:faq")


class FAQDeleteView(DeleteView):
    model = FAQ
    success_url = reverse_lazy("main_app:faq")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class FooterView(ListView):
    template_name = 'admin_info/footer/index.html'
    context_object_name = 'footers'
    queryset = Footer.objects.all()


class FooterUpdateView(UpdateView):
    model = Footer
    template_name = "admin_info/footer/update.html"
    context_object_name = 'footer'
    form_class = FooterForm
    success_url = reverse_lazy("main_app:footer")


class FooterDeleteView(DeleteView):
    model = Footer
    success_url = reverse_lazy("main_app:footer")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)