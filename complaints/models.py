from django.db import models

# Create your models here.

class Engineers(models.Model):
    engineer_name = models.CharField(max_length=200)

    def __str__(self):
    	return self.engineer_name

class Status(models.Model):
    status = models.CharField(max_length=200)

    def __str__(self):
    	return self.status

class Location(models.Model):
	location = models.CharField(max_length = 50)
	def __str__(self):
		return self.location

class Complaint(models.Model):
    status = models.ForeignKey(Status)
    assigned_to = models.ForeignKey(Engineers)
    lock_date = models.DateTimeField('date locked')
    client_name = models.CharField(max_length=200)
    complaint_details = models.CharField(max_length = 500)
    location = models.ForeignKey(Location)

    def __str__(self):
    	return self.complaint_details

class Device(models.Model):
	complaint = models.ForeignKey(Complaint)
	device_name = models.CharField(max_length = 150)
	def __str__(self):
		return self.device_name