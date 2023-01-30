# -*- coding: utf-8 -*-

from django.urls import include, re_path


urlpatterns = [
    re_path(r'^yubin/', include('django_yubin.urls')),
]
