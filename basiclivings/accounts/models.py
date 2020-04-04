from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _


from .managers import UserManager
# Create your models here.


class Packages(models.Model):
    package_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=300, null=False)
    duration = models.PositiveIntegerField(null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "packages"


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = 'city'

    def __str__(self):
        return self.city_name


class Area(models.Model):
    area_id = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=40)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, db_column='city_id')
    pincode = models.CharField(max_length=6, default="")

    class Meta:
        db_table = 'Area'

    def __str__(self):
        return self.area_name


class User(AbstractBaseUser, PermissionsMixin):
    GENDER_LIST = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(_('first name'), max_length=30, unique=False, blank=False, null=False)
    last_name = models.CharField(_('last name'), max_length=30, unique=False, blank=True, null=True)
    email = models.EmailField(_('email'), unique=True, null=False, blank=False)
    gender = models.CharField(_('gender'), choices=GENDER_LIST, blank=False, max_length=10, null=False)
    address = models.CharField(_('address'), blank=False, null=False, max_length=200, default="")
    phone = models.CharField(_('phone'), max_length=10, blank=False, null=False, default="")
    is_pgVendor = models.BooleanField(_('pgVendor'), default=False, blank=False, null=False)
    is_foodVendor = models.BooleanField(_('foodVendor'), default=False, blank=False, null=False)
    is_student = models.BooleanField(_('student'), default=True, blank=False, null=False)
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE, db_column='area_id', blank=True, null=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    email_verified_at = models.DateTimeField(_('email verified at'), blank=True, null=True)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(upload_to='', null=True, blank=True, default="")
    is_staff = models.BooleanField(default=False)
    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'address']

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def short_name(self):
        return self.first_name

    def getuser_id(self):
        return self.user_id

    def get_username(self):
        return self.first_name

    def get_phone(self):
        return str(self.phone)

    def get_gender(self):
        return self.gender

    def get_address(self):
        return self.address

    def email_user(self, subject, message, from_email=None, **kwargs):
        #
        # Sends an email to this User.
        #
        send_mail(subject, message, from_email, [self.email], **kwargs)

    class Meta:
        db_table = "user"

