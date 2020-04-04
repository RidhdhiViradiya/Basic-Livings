from django.contrib import admin
from .models import User, Area, City, Packages
from .forms import UserChangeForm, UserCreationForm
# Register your models here.


admin.site.site_header = "'Basic Livings' Administration"
admin.site.site_title = " Administration Controls"
admin.site.index_title = "Database Tables"


class UserAdmin(admin.ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'first_name', 'last_name', 'phone', 'address', 'is_active')
    list_filter = ('is_active', 'is_pgVendor', 'is_foodVendor', 'is_student', 'area_id')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'gender', 'address', 'phone',)}),
        ('Permissions', {'fields': ('is_pgVendor', 'is_foodVendor', 'is_student', 'is_superuser', 'is_staff',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', 'first_name', 'last_name')
    filter_horizontal = ()

    def set_inactive(self, request, queryset):
        count = queryset.update(is_active=False)
        if count == 1:
            self.message_user(request, "Marked {} User Inactive".format(count))
        else:
            self.message_user(request, "Marked {} Users Inactive".format(count))
    set_inactive.short_description = "Mark Selected as Inactive !!"

    def set_active(self, request, queryset):
        count = queryset.update(is_active=True)
        if count == 1:
            self.message_user(request, "Marked {} User Active".format(count))
        else:
            self.message_user(request, "Marked {} Users Active".format(count))
    set_active.short_description = "Mark Selected as Active !!"

    actions = {'set_inactive', 'set_active'}


class CityAdmin(admin.ModelAdmin):
    list_display = ['city_name']
    ordering = ['city_name']
    search_fields = ['city_name']
    list_per_page = 15


class AreaAdmin(admin.ModelAdmin):
    list_display = ['area_name', 'getCity']

    def getCity(self):
        return self.city_name


admin.site.register(User, UserAdmin)
admin.site.register(Area, AreaAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Packages)
