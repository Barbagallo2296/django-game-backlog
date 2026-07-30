from rest_framework import serializers

from .models import Genere, Gioco, Sviluppatore


class SviluppatoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sviluppatore
        fields = ["id", "nome", "paese"]


class GenereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genere
        fields = ["id", "nome"]


class GiocoSerializer(serializers.ModelSerializer):
    # in lettura: nomi leggibili invece dei codici grezzi
    sviluppatore_nome = serializers.CharField(source="sviluppatore.nome", read_only=True)
    stato_label = serializers.CharField(source="get_stato_display", read_only=True)
    piattaforma_label = serializers.CharField(source="get_piattaforma_display", read_only=True)

    class Meta:
        model = Gioco
        fields = [
            "id", "titolo",
            "piattaforma", "piattaforma_label",
            "stato", "stato_label",
            "ore_giocate", "voto", "note", "data_aggiunta",
            "sviluppatore", "sviluppatore_nome",
            "generi",
        ]

    def validate_voto(self, value):
        if value is not None and not (1 <= value <= 10):
            raise serializers.ValidationError("Il voto deve essere compreso tra 1 e 10.")
        return value