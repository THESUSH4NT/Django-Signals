# Topic: Django Signals


import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
import time

# Sample model
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Signal receiver
@receiver(post_save, sender=MyModel)
def my_signal_receiver(sender, instance, created, **kwargs):
    print(f'Signal received for {instance.name} in thread: {threading.current_thread().name}')
    time.sleep(2)  # Simulating a long process
    print('Signal processing complete in thread:', threading.current_thread().name)

# Usage in a new thread
def save_model():
    obj = MyModel(name='Test Object')
    obj.save()

thread = threading.Thread(target=save_model)
thread.start()
thread.join()

print('This message prints only after the signal processing is complete.')
