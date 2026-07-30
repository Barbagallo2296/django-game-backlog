from django.db import models


class Sviluppatore(models.Model):
    nome = models.CharField(max_length=100)
    paese = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ["nome"]
        verbose_name_plural = "sviluppatori"

    def __str__(self):
        return self.nome


class Genere(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        ordering = ["nome"]
        verbose_name_plural = "generi"

    def __str__(self):
        return self.nome


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
    sviluppatore = models.ForeignKey(
        Sviluppatore,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name="giochi",
    )
    generi = models.ManyToManyField(Genere, blank=True, related_name="giochi")

    class Meta:
        ordering = ["-data_aggiunta"]
        verbose_name_plural = "giochi"

    def __str__(self):
        return self.titolo