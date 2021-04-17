from django import forms
from main.models import *
from django.forms.models import inlineformset_factory


#
# class QuestionForm(forms.ModelForm):
#     class Meta:
#         model = Questions
#         fields = ("question_uz", "answer_uz", "question_ru", "answer_ru", "question_en", "answer_en",)
#
#
# class AnnouncementForm(forms.ModelForm):
#     class Meta:
#         model = Announcement
#         fields = ("title_uz", "description_uz", "title_ru", "description_ru", "title_en", "description_en", "image",)
#
#
# class FooterForm(forms.ModelForm):
#     class Meta:
#         model = Footer
#         fields = ("title_uz", "description_uz", "title_ru", "description_ru", "title_en", "description_en",)
#
#
class NavigationForm(forms.ModelForm):
    class Meta:
        model = Navbar
        fields = ("title", "url", "order",)


class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = (
            "title", "description", "image", "draft", "url"
        )


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = (
            "title", "content", "icon", "url"
        )


class AnonsBarForm(forms.ModelForm):
    class Meta:
        model = AnonsBar
        fields = (
            "description", "image", "is_active", "url"
        )


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = (
            "title", "description", "image", "icon"
        )


class CarrierForm(forms.ModelForm):
    class Meta:
        model = Carriers
        fields = (
            "title", "description", "image"
        )


class CarrierAppForm(forms.ModelForm):
    class Meta:
        model = CarriesApplication
        fields = (
            "description", "image", 'url'
        )


class TruckloadTypeForm(forms.ModelForm):
    class Meta:
        model = TruckloadType
        fields = (
            'title', 'is_available'
        )


class TruckTypeForm(forms.ModelForm):
    class Meta:
        model = TruckType
        fields = (
            'title', 'is_available'
        )


class CargoTypeForm(forms.ModelForm):
    class Meta:
        model = CargoType
        fields = (
            'title', 'is_available'
        )


class CargoWeightForm(forms.ModelForm):
    class Meta:
        model = CargoWeight
        fields = (
            'title',
        )


class ShippersShowForm(forms.ModelForm):
    class Meta:
        model = ShippersForm
        fields = (
            'fullname', 'company', 'pickup_date', 'delivery_date', 'from_city',
            'to_city', 'cargo_weight', 'cargo_type', 'truck_type', 'truckload_type',
            'phone', 'email', 'comments'
        )


class AboutUsForm(forms.ModelForm):
    class Meta:
        model = AboutUs
        fields = (
            'title', 'content', 'subcontent', 'image'
        )


class StatisticsForm(forms.ModelForm):
    class Meta:
        model = Statistics
        fields = (
            'title', 'image', 'quantity'
        )


class AboutUsSectionForm(forms.ModelForm):
    class Meta:
        model = AboutUsSection
        fields = (
            'title', 'content', 'subcontent', 'image'
        )


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = (
            'name', 'surname', 'job_title', 'image', 'twitter', 'facebook', 'telegram', 'instagram'
        )


class InsightForm(forms.ModelForm):
    class Meta:
        model = Insights
        fields = (
            'title', 'content', 'subcontent', 'image'
        )


class CareerForm(forms.ModelForm):
    class Meta:
        model = Careers
        fields = (
            'title', 'content'
        )


class PaymentTypeForm(forms.ModelForm):
    class Meta:
        model = PaymentType
        fields = (
            'payment_type',
        )


class WorkTypeForm(forms.ModelForm):
    class Meta:
        model = WorkType
        fields = (
            'work_type',
        )


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancies
        fields = (
            'job_title', 'company', 'description', 'start_time', 'end_time', 'image', 'payment_type', 'quantity', 'url',
            'work_type', 'work_hour', 'email', 'phone', 'location'
        )


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'fullname', 'email', 'phone'
        )


class PrivacyForm(forms.ModelForm):
    class Meta:
        model = PrivacyPolicy
        fields = (
            'content',
        )


class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = (
            'question', 'answer', 'draft'
        )


class FooterForm(forms.ModelForm):
    class Meta:
        model = Footer
        fields = (
            'phone', 'fax', 'mail', 'short_address', 'full_address', 'copyright', 'twitter', 'telegram', 'facebook',
            'instagram'
        )


class QuoteForm(forms.ModelForm):
    class Meta:
        model = RequestQuote
        fields = (
            'fullname', 'company', 'truckload_type', 'truck_type', 'pickup_date', 'delivery_date', 'from_city',
            'to_city', 'phone', 'email', 'comments'
        )


class CarrierShowForm(forms.ModelForm):
    class Meta:
        model = CarriersForm
        fields = (
            'fullname', 'company', 'truckload_type', 'truck_type', 'pickup_date', 'delivery_date', 'from_city',
            'to_city', 'phone', 'email', 'comments'
        )

#
#
# class NominationForm(forms.ModelForm):
#     class Meta:
#         model = Nomination
#         fields = ("title_uz", "description_uz", "content_uz",
#                   "title_ru", "description_ru", "content_ru",
#                   "title_en", "description_en", "content_ru",
#                   "image",)
#
#
# class StatisticsForm(forms.ModelForm):
#     class Meta:
#         model = Statistics
#         fields = ("title_uz", "title_ru", "title_en", "quantity", "percentage")
#
#
# class JudgeForm(forms.ModelForm):
#     class Meta:
#         model = Judge
#         fields = ("fullname", "image", "jobTitle_uz", "jobTitle_ru", "jobTitle_en")
#
#
# class NewsForm(forms.ModelForm):
#     class Meta:
#         model = News
#         fields = ("title_uz", "description_uz", "content_uz",
#                   "title_ru", "description_ru", "content_ru",
#                   "title_en", "description_en", "content_ru",
#                   "image", "url", "date",)
#
#
# class DateInput(forms.DateInput):
#     input_type = 'date'
#
#
# class ApplicationTeamForm(forms.ModelForm):
#     class Meta:
#         model = ApplicationTeam
#         fields = "__all__"
#         exclude = ("category", "created_at",)
#         widgets = {
#             "title": forms.TextInput(attrs={"class": "form-control"}),
#             "members_count": forms.NumberInput(attrs={"class": "form-control"}),
#             "direction": forms.Select(attrs={"class": "form-control"}),
#             "project_aim": forms.Textarea(attrs={"class": "form-control"}),
#             "project_solution": forms.Textarea(attrs={"class": "form-control"}),
#             "project_content": forms.Textarea(attrs={"class": "form-control"}),
#             "project_budget": forms.Select(attrs={"class": "form-control"}),
#             "project_situation": forms.Select(attrs={"class": "form-control"}),
#             "project_material": forms.FileInput(attrs={"class": "form-control"}),
#             "project_title": forms.TextInput(attrs={"class": "form-control"}),
#         }
#
#
# class ApplicationSelfForm(forms.ModelForm):
#     class Meta:
#         model = ApplicationSelf
#         fields = "__all__"
#         exclude = ("category", "created_at",)
#         widgets = {
#             "fullname": forms.TextInput(attrs={"class": "form-control"}),
#             "date_of_birth": DateInput(attrs={"class": "form-control"}),
#             "passport_serial": forms.TextInput(attrs={"class": "form-control"}),
#             "passport_number": forms.NumberInput(attrs={"class": "form-control"}),
#             "place_work_study": forms.TextInput(attrs={"class": "form-control"}),
#             "phone": forms.TextInput(attrs={"class": "form-control"}),
#             "email": forms.EmailInput(attrs={"class": "form-control"}),
#             "photo": forms.FileInput(attrs={"class": "form-control"}),
#             "direction": forms.Select(attrs={"class": "form-control"}),
#             "project_aim": forms.Textarea(attrs={"class": "form-control"}),
#             "project_solution": forms.Textarea(attrs={"class": "form-control"}),
#             "project_content": forms.Textarea(attrs={"class": "form-control"}),
#             "project_budget": forms.Select(attrs={"class": "form-control"}),
#             "project_situation": forms.Select(attrs={"class": "form-control"}),
#             "project_material": forms.FileInput(attrs={"class": "form-control"}),
#             "project_title": forms.TextInput(attrs={"class": "form-control"}),
#         }
#
#
# class VideosForm(forms.ModelForm):
#     class Meta:
#         model = Videos
#         fields = "__all__"
#         exclude = ("created_at", "title", "category", "views")
#         widgets = {
#             "title_uz": forms.TextInput(attrs={"class": "form-control"}),
#             "title_ru": forms.TextInput(attrs={"class": "form-control"}),
#             "title_en": forms.TextInput(attrs={"class": "form-control"}),
#             "video_url": forms.TextInput(attrs={"class": "form-control"}),
#         }
#
#
# class VideoTutorialsForm(forms.ModelForm):
#     class Meta:
#         model = VideoTutorial
#         fields = "__all__"
#         exclude = ("date", "title", "category", "views")
#         widgets = {
#             "title_uz": forms.TextInput(attrs={"class": "form-control"}),
#             "title_ru": forms.TextInput(attrs={"class": "form-control"}),
#             "title_en": forms.TextInput(attrs={"class": "form-control"}),
#             "video_url": forms.TextInput(attrs={"class": "form-control"}),
#         }
#
#
# class TeamMemberForm(forms.ModelForm):
#     class Meta:
#         model = TeamMember
#         fields = "__all__"
#         exclude = ("category", "created_at",)
#         widgets = {
#             "captain": forms.NullBooleanSelect(attrs={"class": "form-control"}),
#             "date_of_birth": DateInput(attrs={"class": "form-control"}),
#             "passport_serial": forms.TextInput(attrs={"class": "form-control"}),
#             "passport_number": forms.NumberInput(attrs={"class": "form-control"}),
#             "place_work_study": forms.TextInput(attrs={"class": "form-control"}),
#             "phone": forms.TextInput(attrs={"class": "form-control"}),
#             "email": forms.EmailInput(attrs={"class": "form-control"}),
#             "photo": forms.FileInput(attrs={"class": "form-control"}),
#             "fullname": forms.TextInput(attrs={"class": "form-control"}),
#         }
#
#
# class ImagesForm(forms.ModelForm):
#     class Meta:
#         model = ImagesSectionImage
#         fields = "__all__"
#         widgets = {
#             "main_image": forms.FileInput(attrs={"class": "form-control"}),
#         }
#
#
# class MainImageForm(forms.ModelForm):
#     class Meta:
#         model = ImagesSection
#         fields = "__all__"
#         exclude = ("date", "title", "category", "views")
#         widgets = {
#             "title_uz": forms.TextInput(attrs={"class": "form-control"}),
#             "title_ru": forms.TextInput(attrs={"class": "form-control"}),
#             "title_en": forms.TextInput(attrs={"class": "form-control"}),
#             "main_image": forms.FileInput(attrs={"class": "form-control"}),
#             "url" : forms.TextInput(attrs={"class": "form-control"}),
#         }
#
# class CentralCouncilForm(forms.ModelForm):
#     class Meta:
#         model = CentralCouncil
#         fields = "__all__"
#         widgets = {
#             "city": forms.Select(attrs={"class": "form-control"}),
#             "coordinator": forms.TextInput(attrs={"class": "form-control"}),
#             "email": forms.TextInput(attrs={"class": "form-control"}),
#             "phone": forms.TextInput(attrs={"class": "form-control"}),
#         }
#
#
# class WinnersForm(forms.ModelForm):
#     class Meta:
#         model = Winners
#         fields = "__all__"
#         widgets = {
#             "individual": forms.SelectMultiple(attrs={"class": "form-control"}),
#             "team": forms.SelectMultiple(attrs={"class": "form-control" }),
#         }
