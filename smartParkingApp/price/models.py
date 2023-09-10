from djongo import models 
import datetime

class Price(models.Model):
    carPrice = models.IntegerField()
    date_modified = models.DateTimeField(auto_now_add=datetime.datetime.now)

class PriceHistory(models.Model):
    carPrice = models.IntegerField()
    month = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    avgCarOccupancy = models.IntegerField()
