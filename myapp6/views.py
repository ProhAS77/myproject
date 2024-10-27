from django.shortcuts import render
from django.db.models import Sum

from myapp5.models import Product


def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity'))#aggregate(Sum()) - агрегированные функции для  БД
    context = {
        'title': 'Общее кол-во посчитано в БД',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)


def total_in_view(request):
    products = Product.objects.all()
    total = sum(product.quantity for product in products)
    context = {
        'title': 'Общее кол-во посчитано в представлении (view)',
        'total': total,
    }
    return render(request, 'myapp6/total_count.html', context)


def total_in_template(request):
    context = {
        'title': 'Общее кол-во посчитано в шаблоене',
        'products': Product,
    }
    return render(request, 'myapp6/total_count.html', context)
