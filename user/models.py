from django.db import models

# Create your models here.
class user(models.Model):
    u_name = models.CharField(max_length=30)
    address= models.CharField(max_length=60)
    pin_code = models.IntegerField()
    ph_no = models.IntegerField()
    email = models.EmailField(max_length=35)
    password = models.CharField(max_length=10)

    class Meta:
        db_table = '.u_name'
