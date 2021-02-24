from django.db import models

# Create your models here.
class Job(models.Model):
	# Images
	image = models.ImageField(upload_to='images/')
	summary = models.CharField(max_length=10000)
	
	def __str__(self):
		return self.summary
