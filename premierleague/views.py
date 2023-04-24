from django.shortcuts import render
from .models import ManUtd

def index(request):
    all_players_manutd = ManUtd.objects.all()

    #fetching details and saving in dictionary [model to dict]
    from django.core import serializers
    data = serializers.serialize('python', all_players_manutd)

    context = {'data': data}

    return render(request, 'premierleague\index.html', context)
