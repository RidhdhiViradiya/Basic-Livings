from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import CheckConstraint, Q, F
# Create your models here.


class Amenities(models.Model):
    amenities_id = models.AutoField(primary_key=True)
    amenities_name = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        db_table = 'amenities'

    def __str__(self):
        return self.amenities_name


class Room(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender')
    )
    room_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column="user_id")
    address = models.CharField(max_length=200, blank=False, null=False)
    no_of_beds = models.PositiveIntegerField(default=0, null=False, blank=False)
    vacant_beds = models.PositiveIntegerField(default=0, null=False, blank=False)
    rent_per_bed = models.PositiveIntegerField(default=0, null=False, blank=False)
    deposit = models.PositiveIntegerField(default=0, null=True, blank=True)
    available_from = models.DateTimeField(blank=False, null=False)
    # pass amenities names by string
    amenities = models.CharField(max_length=500, default="", null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER, blank=False, null=False)
    area_id = models.ForeignKey('accounts.Area', on_delete=models.CASCADE, db_column="area_id", db_index=True)
    special_instruction = models.CharField(max_length=400, blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    # i have a query here for the expiry fields that: what is the user adds addition rooms in this then what would
    # be the time for other room
    # currently assuming the exp date for the validity of showcasing the entire room on the site!!!
    exp_date = models.DateTimeField(blank=False, null=False)
    is_active = models.BooleanField(default=False, null=False)

    class Meta:
        db_table = 'rooms'
        # constraints = [
        #     CheckConstraint(
        #         check=Q(vacant_beds__lte=F('no_of_beds')), name='check_vacant_bed',
        #     ),
        #     CheckConstraint(
        #         check=Q(available_from__gte=timezone.now), name='check_availability_date',
        #     ),
        #     CheckConstraint(
        #         check=Q(exp_date__gte=timezone.now), name='check_expiry_date',
        #     ),
        # ]

    # def __str__(self):
    #     return 'User: ' + self.user_id.get_full_name() + "\n  Address: " + self.address

    def __str__(self):
        return str(self.room_id)

    def getUserId(self):
        return self.user_id.getuser_id()

    def getRoomId(self):
        return self.room_id

    @property
    def days_since_posted(self):
        return (timezone.now() - self.date_posted).days


class RoomImage(models.Model):
    image_id = models.AutoField(primary_key=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, db_column="room_id")
    image_path = models.ImageField(upload_to='payingGuest/images/', default="")

    class Meta:
        db_table = 'room_images'

    def __str__(self):
        # return "User: " + str(self.room_id.getUserId()) + " Room: " + str(self.room_id.getRoomId())
        return str(self.room_id)


class Watchlist(models.Model):
    watchlist_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column="user_id")
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, db_column="room_id")

    class Meta:
        db_table = 'watchlist'

    def __str__(self):
        return "User: " + self.user_id.get_full_name() + "List No: " + self.watchlist_id


class RoomsVendorPayment(models.Model):
    pay_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column="user_id")
    room_id = models.ForeignKey(Room,  on_delete=models.CASCADE, db_column="room_id")
    no_of_beds = models.PositiveIntegerField()
    amount = models.PositiveIntegerField(null=True, blank=True)
    date_of_payment = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'rooms_vendor_payment'

    def __str__(self):
        return "User: " + self.user_id.get_full_name() + "Payment Number: " + self.pay_id


class RoomsBookingDetail(models.Model):
    booking_id = models.AutoField(primary_key=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, db_column="room_id")
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, db_column="user_id")
    booking_date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'rooms_booking_details'

    def __str__(self):
        return "User: " + self.user_id.get_full_name() + "Booking Number: " + self.booking_id
