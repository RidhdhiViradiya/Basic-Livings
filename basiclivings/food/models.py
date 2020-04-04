from django.db import models
from accounts.models import User, Packages
# Create your models here.


class Tiffin_types(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=30, unique=True)

    # contains types like 2Dabbas, 3Dabbas, 4Dabbas, etc....

    class Meta:
        db_table = 'tiffin_types'


class Mess(models.Model):
    mess_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id')
    mess_name = models.CharField(max_length=250, null=False)
    address = models.CharField(max_length=500, null=False)

    class Meta:
        db_table = 'mess'


categories = [
    ('Veg', 'Veg'),
    ('Non-Veg', 'Non-Veg')
]


class Food_types(models.Model):
    food_id = models.AutoField(primary_key=True)
    mess_id = models.ForeignKey(Mess, on_delete=models.CASCADE, db_column='mess_id')
    tiffin_id = models.ForeignKey(Tiffin_types, on_delete=models.CASCADE, db_column='tiffin_id')
    description = models.CharField(max_length=2048, null=False)
    price = models.PositiveIntegerField(default=0, null=False, blank=False)
    category = models.CharField(max_length=20, choices=categories, default='Veg')
    # include the types of tiffin each mess provides

    class Meta:
        db_table = 'food_types'


class Mess_bookings(models.Model):
    booking_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,  on_delete=models.CASCADE, db_column='user_id')
    mess_id = models.ForeignKey(Mess,  on_delete=models.CASCADE, db_column='mess_id')
    booking_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'mess_bookings'


class MessVendorPayment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    mess_id = models.ForeignKey(Mess,  on_delete=models.CASCADE, db_column='mess_id')
    package_id = models.ForeignKey(Packages,  on_delete=models.CASCADE, db_column='package_id')
    date_of_payment = models.DateTimeField(auto_now_add=True)
    exp_date = models.DateTimeField(auto_now_add=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'mess_vendor_payment'

