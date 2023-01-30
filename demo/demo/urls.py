from django.contrib import admin
from django.urls import include, re_path

from .views import IndexView


urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='home'),
    re_path(r'^yubin/', include('django_yubin.urls')),
    re_path(r'^admin/', admin.site.urls),
]
