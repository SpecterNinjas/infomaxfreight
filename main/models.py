from django.db import models
from datetime import date


class Navbar(models.Model):
    title = models.CharField(max_length=32)
    order = models.IntegerField()
    url = models.CharField(blank=True, null=True, max_length=300)

    class Meta:
        verbose_name = 'Navbar'
        verbose_name_plural = 'Navbar'


class Slider(models.Model):
    title = models.CharField("Title", max_length=512)
    description = models.TextField("Description", max_length=1024)
    image = models.FileField("Image", upload_to='main/slider/')
    draft = models.BooleanField("Draft", default=True)
    url = models.CharField("Url", blank=True, null=True, max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Slider'


class Services(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField(max_length=3000)
    icon = models.FileField(upload_to='main/services/')
    url = models.CharField(blank=True, null=True,max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class AnonsBar(models.Model):
    description = models.TextField(max_length=2048)
    image = models.FileField(upload_to='main/anons_bar/')
    is_active = models.BooleanField(default=True)
    url = models.CharField(blank=True, null=True,max_length=300)

    class Meta:
        verbose_name = 'Anons Bar'
        verbose_name_plural = 'Anons Bar'


class Section(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=1024)
    image = models.FileField(upload_to='main/section/')
    icon = models.FileField(upload_to='main/section/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Section'


class Carriers(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=3000)
    image = models.FileField(upload_to='main/carriers/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Carrier'
        verbose_name_plural = 'Carriers'


class CarriesApplication(models.Model):
    description = models.TextField(max_length=3000)
    image = models.FileField(upload_to='main/subcarriers/')
    url = models.CharField(blank=True, null=True,max_length=300)

    class Meta:
        verbose_name = 'SubCarrier'
        verbose_name_plural = 'SubCarriers'


class TruckloadType(models.Model):
    title = models.CharField(max_length=128)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Truckload Type'
        verbose_name_plural = 'Truckload Types'


class TruckType(models.Model):
    title = models.CharField(max_length=128)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Truck Type'
        verbose_name_plural = 'Truck Types'


class CargoType(models.Model):
    title = models.CharField(max_length=128)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Cargo Type'
        verbose_name_plural = 'Cargo Types'


class CargoWeight(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Cargo Weight'
        verbose_name_plural = 'Cargo Weight'


class ShippersForm(models.Model):
    fullname = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    truckload_type = models.ForeignKey(TruckloadType, on_delete=models.CASCADE)
    truck_type = models.ForeignKey(TruckType, on_delete=models.CASCADE)
    cargo_type = models.ForeignKey(CargoType, on_delete=models.CASCADE)
    cargo_weight = models.ForeignKey(CargoWeight, on_delete=models.CASCADE)
    pickup_date = models.DateField(default=date.today)
    delivery_date = models.DateField(default=date.today)
    from_city = models.CharField(max_length=128)
    to_city = models.CharField(max_length=128)
    phone = models.CharField(max_length=16)
    email = models.EmailField(max_length=64)
    comments = models.TextField(max_length=3000)

    class Meta:
        verbose_name = 'Shipper Form'
        verbose_name_plural = 'Shippers Form'


class AboutUs(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField(max_length=4000)
    subcontent = models.TextField(max_length=2048)
    image = models.FileField(upload_to='main/about_us/')

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'


class Statistics(models.Model):
    title = models.CharField(max_length=32)
    image = models.FileField(upload_to='main/about_us/', blank=True, null=True)
    quantity = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Statistics'
        verbose_name_plural = 'Statistics'


class AboutUsSection(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField(max_length=4000)
    subcontent = models.TextField(max_length=2048)
    image = models.FileField(upload_to='main/about_us/')

    class Meta:
        verbose_name = 'About Us Section'
        verbose_name_plural = 'About Us Section'


class Team(models.Model):
    name = models.CharField(max_length=16)
    surname = models.CharField(max_length=16)
    job_title = models.CharField(max_length=32)
    image = models.FileField(upload_to='main/team/', default='main/team/avatar-default.png')

    # Social media
    twitter = models.URLField(max_length=64, null=True, blank=True)
    facebook = models.URLField(max_length=64, null=True, blank=True)
    telegram = models.URLField(max_length=64, null=True, blank=True)
    instagram = models.URLField(max_length=64, null=True, blank=True)

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Team Members'


class Insights(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField(max_length=4000)
    subcontent = models.TextField(max_length=2048)
    image = models.FileField(upload_to='main/insights/')

    class Meta:
        verbose_name = 'Insights'
        verbose_name_plural = 'Insights'


class Careers(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField(max_length=4000)

    class Meta:
        verbose_name = 'Careers'
        verbose_name_plural = 'Careers'


class PaymentType(models.Model):
    payment_type = models.CharField(max_length=16)

    def __str__(self):
        return self.payment_type

    class Meta:
        verbose_name = 'Payment Type'
        verbose_name_plural = 'Payment Types'


class WorkType(models.Model):
    work_type = models.CharField(max_length=16)

    def __str__(self):
        return self.work_type

    class Meta:
        verbose_name = 'Work Type'
        verbose_name_plural = 'Work Types'


class Vacancies(models.Model):
    job_title = models.CharField(max_length=64)
    company = models.CharField(max_length=64)
    description = models.TextField(max_length=3000)
    start_time = models.TimeField()
    end_time = models.TimeField()
    image = models.FileField(upload_to='main/vacancies/', default='main/vacancies/default.png')
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0)
    url = models.CharField(null=True, blank=True, max_length=300)
    work_type = models.ForeignKey(WorkType, on_delete=models.CASCADE)
    work_hour = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    location = models.CharField(max_length=128)

    def __str__(self):
        return self.job_title

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'


class ContactUs(models.Model):
    fullname = models.CharField(max_length=32)
    email = models.EmailField(max_length=64)
    phone = models.CharField(max_length=16)
    message = models.TextField(max_length=2000)

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'


class RequestQuote(models.Model):
    fullname = models.CharField(max_length=32)
    company = models.CharField(max_length=32)
    truckload_type = models.ForeignKey(TruckloadType, on_delete=models.CASCADE)
    truck_type = models.ForeignKey(TruckType, on_delete=models.CASCADE)
    pickup_date = models.DateField(default=date.today)
    delivery_date = models.DateField(default=date.today)
    from_city = models.CharField(max_length=64)
    to_city = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.EmailField(max_length=32)
    comments = models.TextField(max_length=3000)

    class Meta:
        verbose_name = 'Request Quote'
        verbose_name_plural = 'Request Quotes'


class PrivacyPolicy(models.Model):
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Privacy Policy"

    class Meta:
        verbose_name = 'Privacy Policy'
        verbose_name_plural = 'Privacy Policy'


class FAQ(models.Model):
    question = models.CharField(max_length=64)
    answer = models.TextField(max_length=2000)
    draft = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'


class Footer(models.Model):
    phone = models.CharField(max_length=18)
    fax = models.CharField(max_length=18)
    mail = models.EmailField(max_length=32)
    short_address = models.CharField(max_length=64)
    full_address = models.CharField(max_length=256)
    copyright = models.CharField(max_length=256)

    # Social media
    twitter = models.URLField(max_length=64, null=True, blank=True)
    facebook = models.URLField(max_length=64, null=True, blank=True)
    telegram = models.URLField(max_length=64, null=True, blank=True)
    instagram = models.URLField(max_length=64, null=True, blank=True)

    class Meta:
        verbose_name = 'Footer'
        verbose_name_plural = 'Footer'


class CarriersForm(models.Model):
    fullname = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    truckload_type = models.ForeignKey(TruckloadType, on_delete=models.CASCADE)
    truck_type = models.ForeignKey(TruckType, on_delete=models.CASCADE)
    pickup_date = models.DateField(default=date.today)
    delivery_date = models.DateField(default=date.today)
    from_city = models.CharField(max_length=128)
    to_city = models.CharField(max_length=128)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=64)
    comments = models.TextField(max_length=3000)

    def __str__(self):
        return f"{self.fullname} - {self.company}"

    class Meta:
        verbose_name = "Carrier Form"
        verbose_name_plural = "Carriers Form"
