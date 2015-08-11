from django.db import models

# Create your models here.

class Status(models.Model):
    status = models.CharField(max_length=200)

    def __str__(self):
    	return self.status

class Engineer_status(models.Model):
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.status

class Amc_type(models.Model):
    amc_type = models.CharField(max_length=200)

    def __str__(self):
        return self.amc_type

class Amc_client(models.Model):
    client_name = models.CharField(max_length=200)
    amc_type = models.ForeignKey(Amc_type)
    renewal_date = models.DateTimeField("Renewal date")
    reminder_date = models.DateTimeField("Reminder date")
    
    def __str__(self):
        return self.client_name

class Engineer(models.Model):
    engineer_name = models.CharField(max_length=200)
    engineer_phone = models.CharField(max_length=200)
    engineer_status = models.ForeignKey(Engineer_status)

    def __str__(self):
        return self.engineer_name

class Location(models.Model):
	location = models.CharField(max_length = 50)
	def __str__(self):
		return self.location

class Complaint(models.Model):
    status = models.ForeignKey(Status)
    assigned_to = models.ForeignKey(Engineer)
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