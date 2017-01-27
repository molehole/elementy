from django.db import models
from django.utils import timezone


# Create your models here.
class Elementy(models.Model):
    nr = models.BigIntegerField(blank=False)
    korpus = models.IntegerField(default=0)
    pianka = models.IntegerField(default=0)
    tkanina = models.IntegerField(default=0)
    struktura = models.IntegerField(default=0)
    tkaninySAP = models.IntegerField(default=0)
    czas = models.IntegerField(default=0)
    dominik = models.IntegerField(default=0)

    def __str__(self):
        return str(self.nr)

class Access(models.Model):
    element = models.ForeignKey(Elementy)
    user = models.CharField(max_length=50)
    time = models.DateTimeField(default=timezone.now)
    query = models.TextField()

    def __str__(self):
        return str(self.element)

class SAPImport(models.Model):
    ta = models.IntegerField()
    material = models.ForeignKey(Elementy)
    name = models.TextField()
    scheduledDate = models.DateField()
    createDate = models.DateField()
    createTime = models.TimeField()
    ackDate = models.DateField(null=True)
    ackTime = models.TimeField()    

    def print_status():
        print("""
            Status TA {0}:
            Material = {1}
            Name = {2}
            ScheduledDate = {3}
            CreateDate = {4}
            CreateTime = {5}
            AckDate = {6}
            AckTime = {7}
            """).format(self.ta, self.material, self.name, self.scheduledDate, self.createDate, self.createTime, self.ackDate, self.ackTime)

    def __str__(self):
        return "-".join((str(self.ta), str(self.scheduledDate)))