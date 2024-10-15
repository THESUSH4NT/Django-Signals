# Topic: Django Signals


from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import IntegrityError

# Sample model
class MyModel(models.Model):
    name = models.CharField(max_length=100)

# Sample model demonstrating rollback
class RelatedModel(models.Model):
    my_model = models.ForeignKey(MyModel, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)

# Signal receiver to save another model
@receiver(post_save, sender=MyModel)
def my_signal_receiver(sender, instance, created, **kwargs):
    if created:
        print(f'Saving related object for {instance.name}')
        RelatedModel.objects.create(my_model=instance, description='A' * 300)

# Usage
try:
    with transaction.atomic():
        obj = MyModel(name='Test Object')
        obj.save()
except IntegrityError:
    print('Transaction rolled back due to IntegrityError.')

# Verifying the created object
print(f'Number of RelatedModel objects: {RelatedModel.objects.count()}')
