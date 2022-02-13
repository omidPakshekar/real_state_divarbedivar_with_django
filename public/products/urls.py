from django.urls import path, include

from . import views

app_name = 'products'

urlpatterns = [
    #new
    path('add_file/', views.PrdouctCreateView.as_view(), name='product-create'),
    path('add_frosh/', views.FroshCreateView.as_view(), name='add_frosh'),
    path('add_villa/', views.VillaCreateView.as_view(), name='add_villa'),
    path('add_proje/', views.ProjeMaskoniCreateView.as_view(), name='add_proje'),
    path('add_rhn/', views.RhnCreateView.as_view(), name='add_rhn'),
    path('add_ejare/', views.EjareCreateView.as_view(), name='add_ejare'),

    path('', views.ProductListView.as_view(), name='list-product'),
    path('<slug:category_slug>/', views.ProductListView.as_view(), name='list-product-category'),
    path('<int:id>/<str:slug>/', views.ProductDetailView.as_view(), name='product-detail'),


]
