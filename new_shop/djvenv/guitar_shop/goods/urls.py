from django.urls import path, re_path, include
from . import views

app_name = 'goods'

urlpatterns = [path('', views.main_page, name='main_page'),
               path('catalog/<slug:slug>', views.catalog_details, name='catalog_details'),
               path('instruments/<slug:slug>', views.catalog_details_instruments, name='catalog_details_instruments')
               ]
