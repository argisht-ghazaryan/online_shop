from django.urls import path
from .views import home, category_by_id, search # category_products, categories_list


urlpatterns = [
    path('', home, name='home'),
    # path('categories/', categories_list, name='categories'),
    path('category/<int:pk>/', category_by_id, name='category'),

    # path('category_producrs/<int:pk>/', category_products, name='cat_products'),
    path('search/', search, name='search'),

]
