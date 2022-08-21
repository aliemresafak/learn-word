from django.contrib import admin

from word.models import Word


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ("name", "meaning", "category")
