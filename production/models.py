
from django.db import models

# Create your models here.

class Detail(models.Model):
    product_name = models.CharField(max_length=100)
    abv = models.IntegerField() # alcohol by volume
    ibu = models.IntegerField() # international bittering units
    srm = models.IntegerField() #standard reference method for color

    #modify the str representation of Detail object 
    def __str__(self):
        return self.product_name


class Product(models.Model): #39:12
    product_name = models.CharField(max_length=100)
    on_hand_qty = models.IntegerField()
    price = models.FloatField()
    #relation between tables
    detail_id = models.ForeignKey(Detail, on_delete=models.CASCADE) #45:00 
    #declare key for id
    def __str__(self):
        return self.detail_id

    
# class datetime.date

class Demand_Signal(models.Model):
    demand_score = models.IntegerField()
    detail_id = models.ForeignKey(Detail, on_delete=models.CASCADE) 
    def __str__(self):
        return self.detail_id