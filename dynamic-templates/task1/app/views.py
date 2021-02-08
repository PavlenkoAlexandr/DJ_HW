from django.shortcuts import render
from django.conf import settings
import csv


def inflation_view(request):

    data = []
    template_name = 'inflation.html'
    with open(settings.INFLATION_RUSSIA_CSV, encoding='utf-8') as f:
        file = csv.reader(f, delimiter=';')
        for row in file:
            data.append(row)
    context = {'file': data}

    return render(request, template_name, context)
