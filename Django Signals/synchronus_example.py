# Topic: Django Signals


# Importing modules
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
import time

# Creating a model
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

# Creating a signal receiver
@receiver(post_save, sender=Product)
def product_saved(sender, instance, created, **kwargs):
    print('Product save signal triggered...')
    time.sleep(2) 
    print(f'Product "{instance.name}" saved with price {instance.price}!')

# Main code
if __name__ == "__main__":
    # Creating an instance of Product
    product = Product(name='Gadget', price=29.99)
    
    print('About to save the product.')
    
    product.save()
    
    print('This message appears after the signal is done processing.')
