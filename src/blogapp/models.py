from django.db import models

class Article(models.Model):
	Title=models.CharField(max_length=100)
	Author=models.CharField(max_length=50)
	published_date=models.DateField(null=True, blank=True)
	description=models.TextField(max_length=500, blank=True)


	def __unicode__(self):
		return self.Title
# Create your models here.
