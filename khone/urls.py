from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from home.sitemaps import HomeViewSitemap
from products.sitemaps import ProductViewSitemap, CategoryViewSitemap
from django.contrib.sitemaps.views import sitemap
from django.conf.urls import handler404

handler404 = 'home.views.views_404'

sitemaps = {
    'home' : HomeViewSitemap,
    'product' : ProductViewSitemap,
    'category' :CategoryViewSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('products/', include('products.urls', namespace='products')),
    path('accounts/', include('accounts.urls', namespace='accounts')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
