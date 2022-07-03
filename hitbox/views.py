from django.shortcuts import render
import hitbox
from .models import Leaderboard

def leaderboard(request):
    leaderboard = Leaderboard.objects.all()
    return render(request, 'hitbox/index.html', {'leaderboard': leaderboard})

def game(request):
    leaderboard = Leaderboard.objects.all()
    return render(request, 'hitbox/game.html', {'leaderboard': leaderboard})

def result(request):
    leaderboard = Leaderboard.objects.all()
    return render(request, 'hitbox/leaderboards.html', {'leaderboard': leaderboard})
