from django.db import models

class School(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=250)
    url = models.URLField(max_length=250, blank=True)
    image = models.ImageField(upload_to='portfo/images/')
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name