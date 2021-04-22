from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from main.models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
import requests
from django.contrib import messages


def admin_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                ''' Begin reCAPTCHA validation '''
                recaptcha_response = request.POST.get('g-recaptcha-response')

                data = {
                    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                    'response': recaptcha_response
                }
                r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
                result = r.json()
                ''' End reCAPTCHA validation '''

                if result['success']:
                    login(request, user)
                    return redirect('main_app:main_page')
                else:
                    messages.error(request, 'Invalid reCAPTCHA.')
                    return redirect('main_app:main-admin-login')
            else:
                messages.error(request, "Your account was inactive.")
                return redirect('main_app:main-admin-login')
        else:
            messages.error(request, "Invalid login details given")
            return redirect('main_app:main-admin-login')

    elif request.method == 'GET':
        return render(request, 'admin_info/AdminLogin/index.html')


class MainView(LoginRequiredMixin, ListView):
    queryset = Navbar.objects.all()
    template_name = 'admin_info/main/index.html'


""" Navigation Part """


class NavigationView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/navigation/index.html'
    context_object_name = 'navigation_list'
    queryset = Navbar.objects.all()


class NavigationCreateView(LoginRequiredMixin, ListView):

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


class NavigationUpdateView(LoginRequiredMixin, UpdateView):
    model = Navbar
    template_name = "admin_info/navigation/update.html"
    context_object_name = 'navigation'
    form_class = NavigationForm
    success_url = reverse_lazy("main_app:navigation")


class NavigationDeleteView(LoginRequiredMixin, DeleteView):
    model = Navbar
    success_url = reverse_lazy("main_app:navigation")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


""" End Navigation Part """


class SliderView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/slider/index.html'
    context_object_name = 'slider_list'
    queryset = Slider.objects.all()


class SliderUpdateView(LoginRequiredMixin, UpdateView):
    model = Slider
    template_name = "admin_info/slider/update.html"
    context_object_name = 'slider'
    form_class = SliderForm
    success_url = reverse_lazy("main_app:slider")


class SliderDeleteView(LoginRequiredMixin, DeleteView):
    model = Slider
    success_url = reverse_lazy("main_app:slider")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class SliderCreateView(LoginRequiredMixin, ListView):

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


class ServiceView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/services/index.html'
    context_object_name = 'service_list'
    queryset = Services.objects.all()


class ServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Services
    success_url = reverse_lazy("main_app:service")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ServiceCreateView(LoginRequiredMixin, ListView):

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


class ServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = Services
    template_name = "admin_info/services/update.html"
    context_object_name = 'service'
    form_class = ServiceForm
    success_url = reverse_lazy("main_app:service")


class AnonsBarView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/anonsbar/index.html'
    context_object_name = 'anons_list'
    queryset = AnonsBar.objects.all()


class AnonsBarCreateView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/anonsbar/create.html')

    def post(self, request):
        form = AnonsBarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:anons_bar')
        else:
            return render(request, 'admin_info/anonsbar/create.html', {'form': form})


class AnonsBarUpdateView(LoginRequiredMixin, UpdateView):
    model = AnonsBar
    template_name = "admin_info/anonsbar/update.html"
    context_object_name = 'anonsbar'
    form_class = AnonsBarForm
    success_url = reverse_lazy("main_app:anons_bar")


class AnonsBarDeleteView(LoginRequiredMixin, DeleteView):
    model = AnonsBar
    success_url = reverse_lazy("main_app:anons_bar")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class SectionView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/section/index.html'
    context_object_name = 'section_list'
    queryset = Section.objects.all()


class SectionCreateView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/section/create.html')

    def post(self, request):
        form = SectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:section')
        else:
            return render(request, 'admin_info/section/create.html', {'form': form})


class SectionDeleteView(LoginRequiredMixin, DeleteView):
    model = Section
    success_url = reverse_lazy("main_app:section")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class SectionUpdateView(LoginRequiredMixin, UpdateView):
    model = Section
    template_name = "admin_info/section/update.html"
    context_object_name = 'section'
    form_class = SectionForm
    success_url = reverse_lazy("main_app:section")


class CarrierView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/carriers/index.html'
    context_object_name = 'carriers'
    queryset = Carriers.objects.all()


# class CarrierCreateView(LoginRequiredMixin, ListView):
#
#     def get(self, request, *args, **kwargs):
#         return render(request, 'admin_info/carriers/create.html')
#
#     def post(self, request):
#         form = CarrierForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('main_app:carriers')
#         else:
#             return render(request, 'admin_info/carriers/create.html', {'form': form})

class CarrierCreateView(LoginRequiredMixin, CreateView):
    model = Carriers
    form_class = CarrierForm
    context_object_name = 'carr'
    template_name = 'admin_info/carriers/create.html'
    success_url = reverse_lazy("main_app:carriers")


class CarrierUpdateView(LoginRequiredMixin, UpdateView):
    model = Carriers
    template_name = "admin_info/carriers/update.html"
    context_object_name = 'carrier'
    form_class = CarrierForm
    success_url = reverse_lazy("main_app:carriers")


class CarrierDeleteView(LoginRequiredMixin, DeleteView):
    model = Carriers
    success_url = reverse_lazy("main_app:carriers")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class CarriersAppView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/carriers_application/index.html'
    context_object_name = 'carriers_app'
    queryset = CarriesApplication.objects.all()


class CarrierAppCreateView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/carriers_application/create.html')

    def post(self, request):
        form = CarrierAppForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:carriers_app')
        else:
            return render(request, 'admin_info/carriers_application/create.html', {'form': form})


class CarrierAppUpdateView(LoginRequiredMixin, UpdateView):
    model = CarriesApplication
    template_name = "admin_info/carriers_application/update.html"
    context_object_name = 'carrier_app'
    form_class = CarrierAppForm
    success_url = reverse_lazy("main_app:carriers_app")


class CarrierAppDeleteView(LoginRequiredMixin, DeleteView):
    model = CarriesApplication
    success_url = reverse_lazy("main_app:carriers_app")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class TruckloadTypeView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/truckload_type/index.html'
    context_object_name = 'truckload_types'
    queryset = TruckloadType.objects.all()


class TruckloadTypeCreateView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/truckload_type/create.html')

    def post(self, request):
        form = TruckloadTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:truckload_type')
        else:
            return render(request, 'admin_info/truckload_type/create.html', {'form': form})


class TruckloadTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = TruckloadType
    template_name = "admin_info/truckload_type/update.html"
    context_object_name = 'truckload_type'
    form_class = TruckloadTypeForm
    success_url = reverse_lazy("main_app:truckload_type")


class TruckloadTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = TruckloadType
    success_url = reverse_lazy("main_app:truckload_type")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class TruckTypeView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/truck_type/index.html'
    context_object_name = 'truckload_types'
    queryset = TruckType.objects.all()


class TruckTypeCreateView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/truck_type/create.html')

    def post(self, request):
        form = TruckTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:truck_type')
        else:
            return render(request, 'admin_info/truck_type/create.html', {'form': form})


class TruckTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = TruckType
    template_name = "admin_info/truck_type/update.html"
    context_object_name = 'truck_type'
    form_class = TruckTypeForm
    success_url = reverse_lazy("main_app:truck_type")


class TruckTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = TruckType
    success_url = reverse_lazy("main_app:truck_type")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class CargoTypeView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/cargo_type/index.html'
    context_object_name = 'cargo_types'
    queryset = CargoType.objects.all()


class CargoTypeCreateView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/cargo_type/create.html')

    def post(self, request):
        form = CargoTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:cargo_type')
        else:
            return render(request, 'admin_info/cargo_type/create.html', {'form': form})


class CargoTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = CargoType
    template_name = "admin_info/cargo_type/update.html"
    context_object_name = 'cargo_type'
    form_class = CargoTypeForm
    success_url = reverse_lazy("main_app:cargo_type")


class CargoTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = CargoType
    success_url = reverse_lazy("main_app:cargo_type")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class CargoWeightView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/cargo_weight/index.html'
    context_object_name = 'cargo_weights'
    queryset = CargoWeight.objects.all()


class CargoWeightCreateView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/cargo_weight/create.html')

    def post(self, request):
        form = CargoWeightForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:cargo_weight')
        else:
            return render(request, 'admin_info/cargo_weight/create.html', {'form': form})


class CargoWeightUpdateView(LoginRequiredMixin, UpdateView):
    model = CargoWeight
    template_name = "admin_info/cargo_weight/update.html"
    context_object_name = 'cargo_weight'
    form_class = CargoTypeForm
    success_url = reverse_lazy("main_app:cargo_weight")


class CargoWeightDeleteView(LoginRequiredMixin, DeleteView):
    model = CargoWeight
    success_url = reverse_lazy("main_app:cargo_weight")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ShipperFormDeleteView(LoginRequiredMixin, DeleteView):
    model = ShippersForm
    success_url = reverse_lazy("main_app:shipper_form")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class ShipperFormView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/shipper_form/index.html'
    context_object_name = 'shipper_form'
    queryset = ShippersForm.objects.all()


class ShipperFormUpdateView(LoginRequiredMixin, UpdateView):
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


class AboutUsView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/about_us/index.html'
    context_object_name = 'abouts'
    queryset = AboutUs.objects.all()


# class AboutUsCreateView(LoginRequiredMixin, ListView):
#     model = AboutUs
#
#     def get(self, request, *args, **kwargs):
#         form = AboutUsForm()
#         return render(request, 'admin_info/about_us/create.html' , {"form" : form})
#
#     def post(self, request):
#         form = AboutUsForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('main_app:about_us')
#         else:
#             return render(request, 'admin_info/about_us/create.html', {'form': form})

class AboutUsCreateView(LoginRequiredMixin, CreateView):
    model = AboutUs
    form_class = AboutUsForm
    template_name = "admin_info/about_us/create.html"
    context_object_name = 'about'
    success_url = reverse_lazy("main_app:about_us")


class AboutUsUpdateView(LoginRequiredMixin, UpdateView):
    model = AboutUs
    template_name = "admin_info/about_us/update.html"
    context_object_name = 'about'
    form_class = AboutUsForm
    success_url = reverse_lazy("main_app:about_us")


class AboutUsDeleteView(LoginRequiredMixin, DeleteView):
    model = AboutUs
    success_url = reverse_lazy("main_app:about_us")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class StatisticsView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/statistics/index.html'
    context_object_name = 'statistics'
    queryset = Statistics.objects.all()


class StatisticsCreateView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/statistics/create.html')

    def post(self, request):
        form = StatisticsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:statistics')
        else:
            return render(request, 'admin_info/statistics/create.html', {'form': form})


class StatisticsUpdateView(LoginRequiredMixin, UpdateView):
    model = Statistics
    template_name = "admin_info/statistics/update.html"
    context_object_name = 'statistics'
    form_class = StatisticsForm
    success_url = reverse_lazy("main_app:statistics")


class StatisticsDeleteView(LoginRequiredMixin, DeleteView):
    model = Statistics
    success_url = reverse_lazy("main_app:statistics")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class AboutUsSectionView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/about_us_section/index.html'
    context_object_name = 'abouts'
    queryset = AboutUsSection.objects.all()


# class AboutUsSectionCreateView(LoginRequiredMixin, ListView):
#
#     def get(self, request, *args, **kwargs):
#         return render(request, 'admin_info/about_us_section/create.html')
#
#     def post(self, request):
#         form = AboutUsSectionForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('main_app:about_section')
#         else:
#             return render(request, 'admin_info/about_us_section/create.html', {'form': form})

class AboutUsSectionCreateView(LoginRequiredMixin, CreateView):
    model = AboutUsSection
    form_class = AboutUsSectionForm
    template_name = "admin_info/about_us_section/create.html"
    success_url = reverse_lazy("main_app:about_section")


class AboutUsSectionUpdateView(LoginRequiredMixin, UpdateView):
    model = AboutUsSection
    template_name = "admin_info/about_us_section/update.html"
    context_object_name = 'about'
    form_class = AboutUsSectionForm
    success_url = reverse_lazy("main_app:about_section")


class AboutUsSectionDeleteView(LoginRequiredMixin, DeleteView):
    model = AboutUsSection
    success_url = reverse_lazy("main_app:about_section")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class TeamView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/team/index.html'
    context_object_name = 'team'
    queryset = Team.objects.all()


class TeamCreateView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/team/create.html')

    def post(self, request):
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:team')
        else:
            return render(request, 'admin_info/team/create.html', {'form': form})


class TeamUpdateView(LoginRequiredMixin, UpdateView):
    model = Team
    template_name = "admin_info/team/update.html"
    context_object_name = 'member'
    form_class = TeamForm
    success_url = reverse_lazy("main_app:team")


class TeamDeleteView(LoginRequiredMixin, DeleteView):
    model = Team
    success_url = reverse_lazy("main_app:team")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class InsightView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/insights/index.html'
    context_object_name = 'insight'
    queryset = Insights.objects.all()


# class InsightCreateView(LoginRequiredMixin, ListView):
#
#     def get(self, request, *args, **kwargs):
#         return render(request, 'admin_info/insights/create.html')
#
#     def post(self, request):
#         form = InsightForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('main_app:insight')
#         else:
#             return render(request, 'admin_info/insights/create.html', {'form': form})

class InsightCreateView(LoginRequiredMixin, CreateView):
    model = Insights
    form_class = InsightForm
    template_name = 'admin_info/insights/create.html'
    success_url = reverse_lazy("main_app:insight")

class InsightUpdateView(LoginRequiredMixin, UpdateView):
    model = Insights
    template_name = "admin_info/insights/update.html"
    context_object_name = 'about'
    form_class = InsightForm
    success_url = reverse_lazy("main_app:insight")


class InsightDeleteView(LoginRequiredMixin, DeleteView):
    model = Insights
    success_url = reverse_lazy("main_app:insight")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class CareerView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/careers/index.html'
    context_object_name = 'careers'
    queryset = Careers.objects.all()


# class CareerCreateView(LoginRequiredMixin, ListView):
#
#     def get(self, request, *args, **kwargs):
#         return render(request, 'admin_info/careers/create.html')
#
#     def post(self, request):
#         form = CareerForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('main_app:career')
#         else:
#             return render(request, 'admin_info/careers/create.html', {'form': form})

class CareerCreateView(LoginRequiredMixin,CreateView):
    model = Careers
    form_class = CareerForm
    template_name = 'admin_info/careers/create.html'
    success_url = reverse_lazy('main_app:career')


class CareerUpdateView(LoginRequiredMixin, UpdateView):
    model = Careers
    template_name = "admin_info/careers/update.html"
    context_object_name = 'career'
    form_class = CareerForm
    success_url = reverse_lazy("main_app:career")


class CareerDeleteView(LoginRequiredMixin, DeleteView):
    model = Careers
    success_url = reverse_lazy("main_app:career")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class PaymentTypeCreateView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/payment_type/create.html')

    def post(self, request):
        form = PaymentTypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:payment_type')
        else:
            return render(request, 'admin_info/payment_type/create.html', {'form': form})


class PaymentTypeView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/payment_type/index.html'
    context_object_name = 'cargo_weights'
    queryset = PaymentType.objects.all()


class PaymentTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = PaymentType
    template_name = "admin_info/payment_type/update.html"
    context_object_name = 'payment_type'
    form_class = PaymentTypeForm
    success_url = reverse_lazy("main_app:payment_type")


class PaymentTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = PaymentType
    success_url = reverse_lazy("main_app:payment_type")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class WorkTypeView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/work_type/index.html'
    context_object_name = 'work_types'
    queryset = WorkType.objects.all()


class ShipperFormCreateView(LoginRequiredMixin, ListView):

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


class VacancyCreateView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        form = VacancyForm()
        work_type = WorkType.objects.all()
        payment_type = PaymentType.objects.all()
        return render(request, 'admin_info/vacancies/create.html', {'form':form,'f1': work_type, 'f2': payment_type})

    def post(self, request):
        work_type = WorkType.objects.all()
        payment_type = PaymentType.objects.all()        
        form = VacancyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:vacancy')
        else:
            return render(request, 'admin_info/vacancies/create.html',
                          {'form': form, 'f1': work_type, 'f2': payment_type})


class WorkTypeCreateView(LoginRequiredMixin, ListView):

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


class WorkTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = WorkType
    template_name = "admin_info/work_type/update.html"
    context_object_name = 'work_type'
    form_class = WorkTypeForm
    success_url = reverse_lazy("main_app:work_type")


class WorkTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = WorkType
    success_url = reverse_lazy("main_app:work_type")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class VacancyView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/vacancies/index.html'
    context_object_name = 'vacancies'
    queryset = Vacancies.objects.all()


class ContactUsView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/contact/index.html'
    context_object_name = 'contacts'
    queryset = ContactUs.objects.all()


class ContactUsUpdateView(LoginRequiredMixin, UpdateView):
    model = ContactUs
    template_name = "admin_info/contact/update.html"
    context_object_name = 'contact'
    form_class = ContactForm
    success_url = reverse_lazy("main_app:contact")


class ContactUsDeleteView(LoginRequiredMixin, DeleteView):
    model = ContactUs
    success_url = reverse_lazy("main_app:contact")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class PrivacyPolicyView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/privacy/index.html'
    context_object_name = 'policies'
    queryset = PrivacyPolicy.objects.all()


# class PrivacyPolicyCreateView(LoginRequiredMixin, ListView):
#
#     def get(self, request, *args, **kwargs):
#         return render(request, 'admin_info/privacy/create.html')
#
#     def post(self, request):
#         form = PrivacyForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('main_app:privacy')
#         else:
#             return render(request, 'admin_info/privacy/create.html', {'form': form})

class PrivacyPolicyCreateView(LoginRequiredMixin, CreateView):
    model = PrivacyPolicy
    form_class = PrivacyForm
    success_url = reverse_lazy("main_app:privacy")
    template_name = 'admin_info/privacy/create.html'


class PrivacyPolicyUpdateView(LoginRequiredMixin, UpdateView):
    model = PrivacyPolicy
    template_name = "admin_info/privacy/update.html"
    context_object_name = 'privacy'
    form_class = PrivacyForm
    success_url = reverse_lazy("main_app:privacy")


class PrivacyPolicyDeleteView(LoginRequiredMixin, DeleteView):
    model = PrivacyPolicy
    success_url = reverse_lazy("main_app:privacy")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class FAQView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/faq/index.html'
    context_object_name = 'faqs'
    queryset = FAQ.objects.all()


class FAQCreateView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        return render(request, 'admin_info/faq/create.html')

    def post(self, request):
        form = FAQForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_app:faq')
        else:
            return render(request, 'admin_info/faq/create.html', {'form': form})


class FAQUpdateView(LoginRequiredMixin, UpdateView):
    model = FAQ
    template_name = "admin_info/faq/update.html"
    context_object_name = 'faq'
    form_class = FAQForm
    success_url = reverse_lazy("main_app:faq")


class FAQDeleteView(LoginRequiredMixin, DeleteView):
    model = FAQ
    success_url = reverse_lazy("main_app:faq")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class FooterView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/footer/index.html'
    context_object_name = 'footers'
    queryset = Footer.objects.all()


class FooterUpdateView(LoginRequiredMixin, UpdateView):
    model = Footer
    template_name = "admin_info/footer/update.html"
    context_object_name = 'footer'
    form_class = FooterForm
    success_url = reverse_lazy("main_app:footer")


class FooterDeleteView(LoginRequiredMixin, DeleteView):
    model = Footer
    success_url = reverse_lazy("main_app:footer")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class VacancyUpdateView(LoginRequiredMixin, UpdateView):
    model = Vacancies
    template_name = "admin_info/vacancies/update.html"
    context_object_name = 'vacancies'
    form_class = VacancyForm
    success_url = reverse_lazy("main_app:vacancy")

    def get_context_data(self, **kwargs):
        payment_types = PaymentType.objects.all()
        work_types = WorkType.objects.all()

        context = super(VacancyUpdateView, self).get_context_data(**kwargs)
        context['f1'] = payment_types
        context['f2'] = work_types
        return context


class VacancyDeleteView(LoginRequiredMixin, DeleteView):
    model = Vacancies
    success_url = reverse_lazy("main_app:vacancy")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class RequestQuoteView(ListView):
    template_name = 'admin_info/quote/index.html'
    context_object_name = 'quotes'
    queryset = RequestQuote.objects.all()


class RequestQuoteCreateView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        truckload_types = TruckloadType.objects.all()
        truck_types = TruckType.objects.all()

        return render(request, 'admin_info/quote/create.html', {'f1': truckload_types, 'f2': truck_types})

    def post(self, request):
        form = QuoteForm(request.POST, request.FILES)
        truckload_types = TruckloadType.objects.all()
        truck_types = TruckType.objects.all()

        if form.is_valid():
            form.save()
            return redirect('main_app:quote')
        else:
            return render(request, 'admin_info/quote/create.html',
                          {'form': form, 'f1': truckload_types, 'f2': truck_types})


class RequestQuoteUpdateView(LoginRequiredMixin, UpdateView):
    model = RequestQuote
    template_name = "admin_info/quote/update.html"
    context_object_name = 'quote'
    form_class = QuoteForm
    success_url = reverse_lazy("main_app:quote")

    def get_context_data(self, **kwargs):
        truckLoadTypes = TruckloadType.objects.all()
        truck_types = TruckType.objects.all()

        context = super(RequestQuoteUpdateView, self).get_context_data(**kwargs)
        context['truckload_types'] = truckLoadTypes
        context['f2'] = truck_types
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


class RequestQuoteDeleteView(LoginRequiredMixin, DeleteView):
    model = RequestQuote
    success_url = reverse_lazy("main_app:quote")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class CarriersFormView(LoginRequiredMixin, ListView):
    template_name = 'admin_info/carriers_form/index.html'
    context_object_name = 'carriers_form'
    queryset = CarriersForm.objects.all()


class CarriersFormCreateView(LoginRequiredMixin, ListView):

    def get(self, request, *args, **kwargs):
        truckload_types = TruckloadType.objects.all()
        truck_types = TruckType.objects.all()

        return render(request, 'admin_info/carriers_form/create.html', {'f1': truckload_types, 'f2': truck_types})

    def post(self, request):
        form = CarrierShowForm(request.POST, request.FILES)
        truckload_types = TruckloadType.objects.all()
        truck_types = TruckType.objects.all()

        if form.is_valid():
            form.save()
            return redirect('main_app:carriers_form')
        else:
            return render(request, 'admin_info/carriers_form/create.html',
                          {'form': form, 'f1': truckload_types, 'f2': truck_types})


class CarriersFormUpdateView(LoginRequiredMixin, UpdateView):
    model = CarriersForm
    template_name = "admin_info/carriers_form/update.html"
    context_object_name = 'carriers_form'
    form_class = CarrierShowForm
    success_url = reverse_lazy("main_app:carriers_form")

    def get_context_data(self, **kwargs):
        truckLoadTypes = TruckloadType.objects.all()
        truck_types = TruckType.objects.all()

        context = super(CarriersFormUpdateView, self).get_context_data(**kwargs)
        context['truckload_types'] = truckLoadTypes
        context['f2'] = truck_types
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


class CarriersFormDeleteView(LoginRequiredMixin, DeleteView):
    model = CarriersForm
    success_url = reverse_lazy("main_app:carriers_form")

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
