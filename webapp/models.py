from django.db import models

# Create your models here.

class info(models.Model):
    e = models.CharField(max_length=20)
    p = models.CharField(max_length=20)

    def __str__(self):
        return self.e + "  " +self.p
