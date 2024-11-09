# events/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('event_list', views.event_list, name='event-list'),
    path('event/<int:pk>/', views.event_detail, name='event-detail'),
    path('event/<int:pk>/rsvp/', views.rsvp_event, name='rsvp-event'),
    path('event/<int:pk>/rsvp-list/', views.rsvp_list, name='rsvp-list'),
    path('event/create/', views.create_event, name='create-event'),
    path('event/<int:pk>/edit/', views.update_event, name='update-event'),
    path('event/<int:pk>/delete/', views.delete_event, name='delete-event'),
]
