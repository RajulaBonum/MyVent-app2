# events/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Event(models.Model):
    CATEGORY_CHOICES = (
        ('conference', 'Conference'),
        ('workshop', 'Workshop'),
        ('meetup', 'Meetup'),
        ('webinar', 'Webinar'),
    )

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  # Ensure this field is defined
    title = models.CharField(max_length=200)
    description = models.TextField()
    location_name = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    max_attendees = models.PositiveIntegerField()
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class RSVP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey('Event', on_delete=models.CASCADE)
    status_choices = (
        ('attending', 'Attending'),
        ('not_attending', 'Not Attending')
    )
    status = models.CharField(max_length=20, choices=status_choices)
    rsvp_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')  # Ensure that a user can RSVP to an event only once

    def __str__(self):
        return f'{self.user.username} - {self.event.title} - {self.status}'