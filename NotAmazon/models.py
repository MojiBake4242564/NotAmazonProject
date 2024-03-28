from django.db import models

# Create your models here.
class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=1000)
    item_price = models.FloatField()
    item_rating = models.IntegerField(blank=True)
    item_reviews = models.CharField(max_length=5000, blank=True)



    
    