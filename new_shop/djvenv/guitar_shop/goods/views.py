from django.shortcuts import render, get_object_or_404
from .models import *

#goods_all - это related_name
def main_page(request):
    all_categories = CategoryGoods.objects.all()    # выводит список доступных видов товаров на главной странице
    return render(request, 'goods/catalog_of_goods.html', {'all_categories':all_categories})

def catalog_details(request, slug):
    # ------------------------------#
    # Добавить постраничную разбивку#
    # ------------------------------#
    insruments_catalog = get_object_or_404(CategoryGoods, slug=slug)
    product_sections = insruments_catalog.goods_all.all()
    return render(request, 'goods/catalog_details.html', {'product_sections':product_sections})

def catalog_details_instruments(request, slug):
    # ------------------------------#
    # Добавить постраничную разбивку#
    # ------------------------------#
    instrument = AllGoods.objects.filter(slug=slug)

    get_instrument = get_object_or_404(AllGoods, slug=slug)
    describtion = get_instrument.describe.all()
    return render(request, 'goods/catalog_details_instruments.html', {'instrument':instrument, 'describtion':describtion})



    

