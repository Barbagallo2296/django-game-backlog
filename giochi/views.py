from django.shortcuts import get_object_or_404, render

from .models import Gioco


def lista_giochi(request):
    giochi = Gioco.objects.all()
    return render(request, "giochi/lista_giochi.html", {"giochi": giochi})

def dettaglio_gioco(request, gioco_id):
    gioco = get_object_or_404(Gioco, pk=gioco_id)
    return render(request, "giochi/dettaglio_gioco.html", {"gioco": gioco})