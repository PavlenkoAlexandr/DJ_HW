import csv
import urllib.parse

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from django.conf import settings


def index(request):
    return redirect(reverse(bus_stations))


stations = []
with open(settings.BUS_STATION_CSV, newline='', encoding='cp1251') as f:
    reader = csv.DictReader(f)
    for row in reader:
        stations.append([row['Name'], row['Street'], row['District']])


def bus_stations(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(stations, settings.STATION_PER_PAGE)
    page = paginator.get_page(page_number)
    prev_page_url, next_page_url = None, None
    if page.has_previous():
        prev_page_url = reverse(bus_stations) + '?' + urllib.parse.urlencode({'page':page.previous_page_number()})
    if page.has_next():
        next_page_url = reverse(bus_stations) + '?' + urllib.parse.urlencode({'page':page.next_page_number()})
    return render(request, 'index.html', context={
        'bus_stations': [{'Name': row[0], 'Street': row[1], 'District': row[2]} for row in page.object_list],
        'current_page': page_number,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

