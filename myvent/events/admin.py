# events/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Event, RSVP, User

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'organizer', 'date', 'location_name', 'max_attendees')
    search_fields = ('title', 'location_name', 'organizer__username')  # Search by title, location, and organizer
    list_filter = ('date', 'category', 'organizer')  # Filters by date, category, and organizer

    def has_delete_permission(self, request, obj=None):
        # Allow deletion only for superusers
        return request.user.is_superuser

    def has_add_permission(self, request):
        # Allow only certain users to add events (e.g., based on a custom group or permission)
        return request.user.groups.filter(name='Event Managers').exists() or request.user.is_superuser
    
class RSVPAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'status', 'rsvp_date')
    search_fields = ('user__username', 'event__title')  # Search by user and event title
    list_filter = ('status', 'rsvp_date')  # Filter RSVPs by status and date

class RSVPInline(admin.TabularInline):
    model = RSVP
    extra = 0  # No extra blank fields
    readonly_fields = ('user', 'status', 'rsvp_date')  # RSVP fields to display

class EventInline(admin.TabularInline):
    model = Event
    extra = 0
    fields = ('title', 'date', 'category')  # Display relevant fields

class RSVPInline(admin.TabularInline):
    model = RSVP
    extra = 0
    fields = ('event', 'status', 'rsvp_date')  # Display RSVP details

class CustomUserAdmin(UserAdmin):
    inlines = [EventInline, RSVPInline]  # Add events and RSVPs inline on user admin page

admin.site.register(Event, EventAdmin)
admin.site.register(RSVP, RSVPAdmin)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)