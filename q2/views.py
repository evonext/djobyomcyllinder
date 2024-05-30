import math

from django.shortcuts import render


def home(request):
    return render(request, "index.html")




def cylinder_volume_calculator(request):
    base_radius = ""
    cylinder_height = ""
    cylinder_volume = ""

    if request.method == "POST":
        base_radius = request.POST.get("base_radius")
        cylinder_height = request.POST.get("cylinder_height")
        button = request.POST.get("button")

        if button == "Очистить":
            base_radius = ""
            cylinder_height = ""

        elif button == "Вычислить" and len(base_radius) > 0 and len(cylinder_height) > 0:
            cylinder_volume = round(math.pi * pow(int(base_radius), 2) * int(cylinder_height), 2)

    context = {"base_radius": base_radius, "cylinder_height": cylinder_height, "cylinder_volume": cylinder_volume}
    return render(request, "cylinder_volume_calculator.html", context)
