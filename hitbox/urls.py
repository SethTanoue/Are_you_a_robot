from django.urls import path
from . import views

app_name = 'hitbox'

urlpatterns = [
    path('', views.leaderboard, name='welcome'),
    path('', views.leaderboard, name='welcome'),
    path('', views.leaderboard, name='welcome'),
]
