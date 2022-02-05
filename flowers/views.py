from django.shortcuts import render
from .models import Plant, Shop
from .forms import PlantAdd
from django.views.decorators.csrf import csrf_exempt


def plants_list(request):
    plants = Plant.objects.all()
    ctx = {
        "plants": plants,
    }
    return render(request, "plants.html", ctx)

def home(request):
    shop = Shop.objects.first()
    ctx = {
        "shop": shop
    }
    return render(request, "home.html", ctx)

@csrf_exempt
def plants_add(request):
    if request.method == 'POST':
        form = PlantAdd(request.POST)
        if form.is_valid():
            form.save()
            plants = Plant.objects.all()
            return render(request, "plants.html", {"plants": plants})

    else:
        form = PlantAdd()

    return render(request, 'addplant.html', {'form': form})

@csrf_exempt
def plants_delete(request):
    plants = Plant.objects.all()
    return render(request, 'deleteplant.html', {"plants": plants})

@csrf_exempt
def plants_delete_pk(request, pk):
    plants = Plant.objects.filter(pk=pk).delete()
    plants = Plant.objects.all()
    return render(request, 'deleteplant.html', {"plants": plants})
    