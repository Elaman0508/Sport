from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as yasg_urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('bilimkana/', include('bilimkana.urls')),
    path('marketing/', include('marketing.urls')),

    path('main/', include('main.urls')),

    path('main/', include('main.urls')),
    path('personal/', include('personal.urls')),
    path('boxing/', include('boxing.urls')),
    path('bike/', include('bike.urls')),
    path('relax/', include('yoga.urls')),
    path('tennis/', include('tennis.urls')),
    path('swim/', include('swim.urls')),
    path('tekwando/', include('tekwando.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
