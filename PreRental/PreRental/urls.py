from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("events.urls")),
    #path("signin/", include('django.contrib.auth.urls')),
    #path("signin/", include("Login.urls")),
]
