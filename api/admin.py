from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import URL, User


admin.site.register(URL)


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'id', 'online')
    readonly_fields = ('id',)
    list_filter = ('online', )


admin.site.register(User, CustomUserAdmin)
