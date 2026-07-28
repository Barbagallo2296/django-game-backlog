from django.contrib import admin

from .models import Gioco


@admin.register(Gioco)
class GiocoAdmin(admin.ModelAdmin):
    list_display = ("titolo", "piattaforma", "stato", "ore_giocate", "voto")
    list_filter = ("stato", "piattaforma")
    search_fields = ("titolo",)