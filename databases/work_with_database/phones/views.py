from django.shortcuts import render

from phones.models import Phone
phones = Phone.objects.all()

sort_method = {
    'Названию': 'name',
    'Начиная с дешёвых': 'min_price',
    'Начиная с дорогих': 'max_price'
}

def show_catalog(request):
    sort = request.GET.get('sort', None)
    template = 'catalog.html'
    if sort == 'name':
        phones = Phone.objects.order_by('name').all()
    elif sort == 'min_price':
        phones = Phone.objects.order_by('price').all()
    elif sort == 'max_price':
        phones = Phone.objects.order_by('-price').all()
    context = {'phones': list(phones),
               'sort_method':sort_method}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = [phone for phone in list(phones) if phone.slug == slug][0]
    context = {'phone': phone,
               'slug': slug}
    return render(request, template, context)
