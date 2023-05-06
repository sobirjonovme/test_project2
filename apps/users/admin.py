from django.contrib import admin

from apps.users.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    search_fields = ("first_name", "last_name")
    list_display = ("id", "first_name", "last_name")
    list_display_links = (
        "id",
    )

    fieldsets = (
        ("Personal info", {"fields": ("id", "first_name", "last_name", "is_deleted")}),
        ("Contact info", {"fields": ("email",)}),
        ("Permissions", {"fields": ("is_staff", "is_superuser", "groups", "user_permissions")}),
        (
            "Other",
            {
                "fields": (
                    "is_active",
                    "password",
                )
            },
        ),
        ("Important dates", {"fields": ("date_joined", "last_login", "updated_at")}),
    )
    readonly_fields = (
        "id",
        "updated_at",
    )


# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
