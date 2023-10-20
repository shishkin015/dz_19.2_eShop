from django.shortcuts import render

from catalog.models import Product, Category


# Create your views here.
def index(request):
    catalog_list = Product.objects.all()
    category_list = Category.objects.all()
    context = {
        'product_list': catalog_list,
        'category_list': category_list,
        'title': 'Каталог'
    }
    return render(request, 'catalog/home.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}\n{phone}\n{message}')

    context = {'title': 'Контакт'}
    return render(request, 'catalog/contacts.html', context)
