from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as yasg_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('api/', include('bilimkana.urls')),
    path('api/', include('marketing.urls')),
    path('api/', include('main.urls'))

]
urlpatterns += yasg_urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
