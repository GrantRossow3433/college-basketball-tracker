from django.db.models import Q
from django.shortcuts import redirect, render

from .forms import GameForm
from .models import Game


def game_list(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("game_list")
    else:
        form = GameForm()

    query = request.GET.get("q", "").strip()
    games = Game.objects.all()

    if query:
        games = games.filter(
            Q(away_team__icontains=query)
            | Q(home_team__icontains=query)
            | Q(tv_channel__icontains=query)
            | Q(notes__icontains=query)
        )

    return render(
        request,
        "games/game_list.html",
        {"form": form, "games": games, "query": query},
    )

