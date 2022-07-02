from django.shortcuts import render

import hitbox
from .models import Leaderboard

def leaderboard(request):
    leaderboard = Leaderboard.objects.all()
    return render(request, {'leaderboard': leaderboard})
