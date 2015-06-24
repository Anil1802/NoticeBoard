from django.db import models

# Create your models here.

class Event(models.Model):

	#creating column
	event_name = models.CharField(max_length = 75)
	event_decription = models.CharField(max_length=1500)
	event_date = models.DateField()
	event_timings = models.TimeField()
	event_venue = models.CharField(max_length=75)
	event_fees = models.IntegerField(default = 0)
	event_seats = models.IntegerField(default = 30)
	event_organizer_details =models.CharField(max_length=200) 
 	 		