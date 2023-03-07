from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import settings
from .swagger import ulrpatterns as doc_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/orders/', include("orders.urls")),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/products/', include('products.urls')),
    path('api/v1/cart/', include('cart.urls')),
]

urlpatterns += doc_urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
