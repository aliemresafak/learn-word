from django.contrib import admin

from category.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created", "updated")

    @admin.display()
    def created(self, obj):
        return obj.created_at.strftime("%d-%m-%Y %H:%M:%S")

    @admin.display
    def updated(self, obj):
        return obj.updated_at.strftime("%d-%m-%Y %H:%M:%S")
