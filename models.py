from typing import Iterable
from django.db import models

class Video(models.Model):
    # app_label='speedTest'
    name= models.CharField(max_length=500)
    videofile= models.FileField(upload_to='videos/', null=True, blank=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.videofile)
    
