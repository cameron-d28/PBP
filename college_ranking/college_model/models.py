from django.db import models

# Create your models here.


class College(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50)

    def __str__(self):
        return self.name