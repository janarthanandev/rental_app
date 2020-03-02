from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models


class Home(models.Model):
    RENTSTATUS = (
            ('avail', 'Available'),
            ('navail', 'Not Available'),
        )
    name = models.CharField(max_length=200)
    bedroom = models.IntegerField()
    bathroom = models.IntegerField()
    area = models.CharField(max_length=30)
    rent_expected = models.IntegerField()
    advance_expected = models.IntegerField()
    image_url = models.ImageField()
    rental_status = models.CharField(max_length=20, choices=RENTSTATUS)
    # created_by = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    pass
    class Meta:
        db_table = 'auth_user'
    

    def __str__(self):
        return self.username