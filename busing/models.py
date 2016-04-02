from django.db import models

# Create your models here.

class Stop(models.Model):
	id = models.IntegerField(primary_key=True)
	SHUTTLES = (
		('1', 'Deerfield'),
		('2', 'Broomfield'),
		('3', 'Maroon'),
		('4', 'Gold'),
	)
	shuttle = models.CharField(max_length=200, choices = SHUTTLES)
	location = models.CharField(max_length=200)
	time_1 = models.CharField(max_length=200)
	time_2 = models.CharField(max_length=200)
	REQUEST = (
		('1', 'Every 1/2 Hour'),
		('2', 'Upon Request'),
	)
	type_of_request = models.CharField(max_length=200, choices = REQUEST)
	KIND = (
		('1', 'Bus Stop'),
		('2', 'Apartment'),
		('3', 'Request Stop ($1.00)'),
		('4', 'Request Stop ($2.00)'),
	)
	kind_of_stop = models.CharField(max_length=200, choices = KIND)

	coord_x = models.FloatField(default=43.590579)
	coord_y = models.FloatField(default=-84.775928)
	location_notes = models.CharField(blank=True, null=True, max_length="500", default="No additional notes")

	def __unicode__(self):
		return self.location

