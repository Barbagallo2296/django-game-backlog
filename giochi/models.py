from django.db import models


class Gioco(models.Model):
    class Stato(models.TextChoices):
        DA_GIOCARE = "DA_GIOCARE", "Da giocare"
        IN_CORSO = "IN_CORSO", "In corso"
        FINITO = "FINITO", "Finito"
        ABBANDONATO = "ABBANDONATO", "Abbandonato"

    class Piattaforma(models.TextChoices):
        PC = "PC", "PC"
        PS5 = "PS5", "PlayStation 5"
        XBOX = "XBOX", "Xbox Series"
        SWITCH = "SWITCH", "Nintendo Switch"

    titolo = models.CharField(max_length=200)
    piattaforma = models.CharField(
        max_length=10,
        choices=Piattaforma.choices,
        default=Piattaforma.PC,
    )
    stato = models.CharField(
        max_length=12,
        choices=Stato.choices,
        default=Stato.DA_GIOCARE,
    )
    ore_giocate = models.PositiveIntegerField(default=0)
    voto = models.PositiveSmallIntegerField(null=True, blank=True)
    note = models.TextField(blank=True)
    data_aggiunta = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-data_aggiunta"]

    def __str__(self):
        return self.titolo