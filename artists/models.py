from django.db import models
from django.contrib import admin



class Artist(models.Model):
	artistname = models.CharField(max_length=30)
	GENRE_CHOICES = (
		(u'rock', u'rock'),
		(u'pop', u'pop'),
		(u'hiphop', u'hiphop'),
		(u'latin', u'latin'),
		(u'electronic', u'electronic'),
		(u'other', u'other'),
	)
	zipcode = models.CharField(max_length=10)
	genre = models.CharField(max_length=10, choices=GENRE_CHOICES)
	
	def __unicode__(self):
		return self.artistname
	

class Album(models.Model):
    Artist = models.ForeignKey(Artist)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
	
	
class Song(models.Model):
	Album = models.ForeignKey(Album)
	name = models.CharField(max_length=100)
	upvotes = models.IntegerField(blank=True, null=True)
	downvotes = models.IntegerField(blank=True, null=True)