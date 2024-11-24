from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    flag_image = models.ImageField(upload_to='flags/', blank=True, null=True)  

    def __str__(self):
        return self.name