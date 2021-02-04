from collections import Counter

from django.shortcuts import render
counter_show = Counter()
counter_click = Counter()


def index(request):
    param = request.GET.get('from-landing')
    counter_click[param] += 1
    return render(request, 'index.html')


def landing(request):
    param = request.GET.get('ab-test-arg', 'original')
    if param == 'test':
        template = 'landing_alternate.html'
    else:
        template = 'landing.html'
    counter_show[param] += 1
    return render(request, template)


def stats(request):
    try:
        test_conversion = counter_click['test']/counter_show['test']
    except ZeroDivisionError:
        test_conversion = 'Нет данных'
    try:
        original_conversion = counter_click['original']/counter_show['original']
    except ZeroDivisionError:
        original_conversion = 'Нет данных'

    return render(request, 'stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
