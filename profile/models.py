from django.db import models
from django.contrib.auth.models import User
#from artists.models import Artist

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	zipcode = models.CharField(max_length=10)
#	artist_group = models.ManyToManyField(Artist)
	upvotes = models.CommaSeparatedIntegerField(max_length=1000)
	downvotes = models.CommaSeparatedIntegerField(max_length=1000)
	
	def __unicode__(self):
		return u"%s %s" % (self.firstname, self.lastname)

	def get_firstname(self):
		return u"%s" % (self.firstname)	
		
	def get_fields(self):
		list = [(field.name, field.value_to_string(self)) for field in UserProfile._meta.fields]
		list = list[2:]
		return list
	
	def vote_up(self, song_id):
		return 1 
		
	def vote_down(self, song_id):
		return 1
	
	def get_upvotes(self):
		return 1
		
	def get_downvotes(self):
		return 1
	
