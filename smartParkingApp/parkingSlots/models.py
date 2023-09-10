from djongo import models

class Slot(models.Model):
    sensorNo = models.IntegerField()
    plotNo = models.IntegerField()
    status = models.CharField(max_length=50)