from django.db import models


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=255, null=False, blank=True)
    description = models.TextField(max_length=255, default='', blank=True)
    amount = models.IntegerField(default='1', null=False)
    category = models.ForeignKey(Categories, related_name='products', on_delete=models.CASCADE)
