from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from apps.models import User, New, Category


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = 'user_image', 'email', 'username', 'first_name', 'last_name'
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email", 'image')}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ('first_name', 'phone', "password1", "password2"),
            },
        ),
    )

    def user_image(self, obj: User):
        if obj.image:
            return format_html(
                f'<a href="{obj.pk}">'
                f'<img src="{obj.image.url}" width="35" height="35" style="object-fit: cover; border-radius: 50%"></a>'
            )
        return format_html(
            f'<a href="{obj.pk}">'
            f'<img src="https://t3.ftcdn.net/jpg/03/58/90/78/360_F_358907879_Vdu96gF4XVhjCZxN2kCG0THTsSQi8IhT.jpg"'
            f'width="35" height="35" style="object-fit: cover; border-radius: 50%"></a>'
        )

    user_image.short_description = 'Image'


@admin.register(New)
class NewsModelAdmin(ModelAdmin):
    list_display = ('title', 'author', 'created_at')


@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    list_display = ('name',)
