from django.contrib import admin

from apps.task4.models import PhoneNumber


# Register your models here.
@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone_number")
