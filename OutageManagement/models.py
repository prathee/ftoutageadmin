from django.db import models

# Create your models here.

from django.urls import reverse  # Used to generate urls by reversing the URL patterns
from django.contrib.auth.models import User


class Outage_Service( models.Model ):

    Service = models.CharField( max_length=60, blank=True )
    Outage_ID = models.CharField( max_length=100, blank=True )

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.Service


class Outage( models.Model ):
    """
    Model representing a Outage.
    """

    Service = models.ForeignKey( Outage_Service, null=True, on_delete=models.SET_NULL )
    Prompt_Name = models.TextField( max_length=1000, help_text="Enter the corrosponding OutageManagement prompt file name " )
    Outage_ID = models.CharField( max_length=200, help_text="Enter Outage Servcie Name" )
    Start_Date = models.DateTimeField( null=True, blank=False )
    End_Date = models.DateTimeField( null=True, blank=False )
    Enable_Flag = models.BooleanField()
    Created_By = models.OneToOneField( User, null=True, blank=True, on_delete=models.SET_NULL )

    def get_absolute_url(self):
        """
        Returns the url to access a particular OutageManagement instance.
        """
        return reverse( 'OutageManagement-detail', args=[str( self.id )] )

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.Outage_ID
