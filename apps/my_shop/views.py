from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.db.models import Count


from apps.my_shop.forms import SearchForm
from apps.products.models import Product, Categories, Brand
from django.core.paginator import Paginator


def home(request):
    products = Product.objects.all().order_by('pk')
    cats = Categories.objects.all()
    brands = Brand.objects.all()
    product_count = Categories.objects.annotate(Count('product')).order_by('pk')
    # cat = get_object_or_404(Categories)
    # paginator = Paginator(products, 3)
    # page_number = request.GET.get("page")
    # products = paginator.get_page(page_number)
    return render(request, 'my_shop/index.html', context={'products': products,
                                                          'categories': cats,
                                                          'brands': brands,
                                                          'title': 'Online_shop',
                                                          'product_count': product_count})

#
# def categories_list(request):
#     cats = Categories.objects.all()
#     return render(request, 'my_shop/index.html', context={'cats': cats})


def category_by_id(request, pk):
    cats = Categories.objects.all()
    cat = get_object_or_404(Categories, id=pk)
    filter_products = Product.objects.filter(categories=cat)
    product_count = Categories.objects.annotate(Count('product')).order_by('pk')

    paginator = Paginator(filter_products, 3)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    return render(request, 'my_shop/index.html', context={'filter_products': products,
                                                          'categories': cats,
                                                          'category_selected': cat.pk,
                                                          'product_count': product_count})

#
# def category_products(request, pk):
#     cat = Product.objects.filter(categories=pk)
#     return render(request, 'product/category_products.html', context={'cat': cat})
#


def search(request):
    products = []
    form = SearchForm(request.GET)
    product_count = Categories.objects.annotate(Count('product')).order_by('pk')
    if form.is_valid():
        search_query = form.cleaned_data['search_query'].upper()
        products = Product.objects.filter(Q(name__icontains=search_query) | Q(model__icontains=search_query) |
                                          Q(color__icontains=search_query) | Q(categories__name=search_query))
    return render(request, 'my_shop/search.html', context={'form': form, 'products': products,
                                                           'product_count': product_count})
