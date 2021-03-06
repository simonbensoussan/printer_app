from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Bucketlist(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=255, blank=False, unique=True,default="")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
    
    class Meta:
        """test for admin interface"""
        verbose_name_plural = "Ma list de courses"