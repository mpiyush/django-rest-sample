from django.db import models

# Create your models here.


class Server(models.Model):
    '''
    defines the paramaters of a server
    '''

    name = models.CharField(unique=True, blank=False, max_length=200)
    latitute = models.DecimalField(max_digits=8, decimal_places=3,)
    longitude = models.DecimalField(max_digits=8, decimal_places=3,)

    def __unicode__(self):
        return self.name
