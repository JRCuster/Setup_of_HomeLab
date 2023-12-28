from django.shortcuts import render
from .models import Dragon, Treasure

def index(request):
    dragons = Dragon.objects.all()
    treasures = Treasure.objects.all()
    return render(request, 'dashboard/index.html', {'dragons': dragons, 'treasures': treasures})
