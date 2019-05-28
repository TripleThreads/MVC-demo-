from django.db import models


class Bedroom(models.Model):
    room_id = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rented = models.BooleanField()
    how_long = models.IntegerField()

    def __str__(self):
        return self.room_id
