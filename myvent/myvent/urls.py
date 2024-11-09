# myvent/urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from events.views import landing_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('events.urls')),
    path('users/', include('users.urls')),
    path('', landing_page, name='landing-page'),  # Route for the landing page
]
