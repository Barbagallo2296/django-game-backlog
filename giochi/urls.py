from django.urls import path

from . import views

app_name = "giochi"

urlpatterns = [
    path("", views.lista_giochi, name="lista"),
    path("<int:gioco_id>/", views.dettaglio_gioco, name="dettaglio"),
]