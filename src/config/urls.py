"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]