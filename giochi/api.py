from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.db.models import Avg, Count, Sum

from .models import Genere, Gioco, Sviluppatore
from .serializers import GenereSerializer, GiocoSerializer, SviluppatoreSerializer


class GiocoViewSet(viewsets.ModelViewSet):
    queryset = Gioco.objects.all()
    serializer_class = GiocoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=False)
    def statistiche(self, request):
        qs = Gioco.objects.all()
        dati = {
            "totale_giochi": qs.count(),
            "ore_totali": qs.aggregate(tot=Sum("ore_giocate"))["tot"] or 0,
            "voto_medio": round(qs.aggregate(m=Avg("voto"))["m"] or 0, 2),
            "per_stato": {
                r["stato"]: r["n"]
                for r in qs.values("stato").annotate(n=Count("id"))
            },
        }
        return Response(dati)


class SviluppatoreViewSet(viewsets.ModelViewSet):
    queryset = Sviluppatore.objects.all()
    serializer_class = SviluppatoreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class GenereViewSet(viewsets.ModelViewSet):
    queryset = Genere.objects.all()
    serializer_class = GenereSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]