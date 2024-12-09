
import django
from django.conf.urls import include
from django.urls import re_path as url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls) if django.VERSION < (1, 10) else admin.site.urls),
    #url(r'^accounts/', include('registration.urls')), почему-то не видит модуль
    url(r'^', include('pybb.urls', namespace='pybb')),
]
