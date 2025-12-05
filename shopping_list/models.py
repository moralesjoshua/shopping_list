from django.db import models

# Create your models here.
class ShoppingItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    priority = models.IntegerField(default=1)
    purchased = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name