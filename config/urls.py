from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/sermon/', include("sermon.urls")),
    path('api/auth/', include('authentication.urls')),
    path('api/series/', include('series.urls')),
    path('api/categories/', include('categories.urls')),
]