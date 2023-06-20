
from django.conf import Settings, settings
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from store.api import views as api 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products', api.ProductList.as_view(), name="product_list"),
    path('', include('store.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)