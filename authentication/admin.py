from django.contrib import admin
from authentication.models import User
from datetime import datetime


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "joined_date")

    @admin.display()
    def joined_date(self, obj):
        return obj.date_joined.strftime("%d-%m-%Y %H:%M:%S")
