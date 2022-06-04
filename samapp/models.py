from django.db import models

class Image(models.Model):
    Password = models.CharField(max_length=20)
    Data = models.CharField(max_length=200)
    image1 = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.title

