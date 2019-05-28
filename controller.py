from django.shortcuts import render


def index(request):
    bedrooms = Bedroom.objects.all()

    check_availability(bedrooms)

    context = {
        "bedrooms": bedrooms
    }
    return render(request, 'bedrooms.html', context)


