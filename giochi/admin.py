from django.contrib import admin

from .models import Genere, Gioco, Sviluppatore


@admin.register(Gioco)
class GiocoAdmin(admin.ModelAdmin):
    list_display = ("titolo", "piattaforma", "stato", "sviluppatore", "ore_giocate", "voto")
    list_filter = ("stato", "piattaforma", "generi")
    search_fields = ("titolo",)
    filter_horizontal = ("generi",)


@admin.register(Sviluppatore)
class SviluppatoreAdmin(admin.ModelAdmin):
    list_display = ("nome", "paese")
    search_fields = ("nome",)


@admin.register(Genere)
class GenereAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    search_fields = ("nome",)