# myvent/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('users/', include('users.urls')),
]
