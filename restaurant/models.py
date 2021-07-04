from django.db import models

# Create your models here.

class Restaurant(models.Model):
    r_name = models.CharField(max_length=50)
    r_town = models.CharField(max_length=50)
    r_mobile = models.IntegerField()
    r_pass = models.CharField(max_length=12, default="ADMIN")
    r_email = models.EmailField(max_length=50)
    r_image = models.ImageField(upload_to="restaurant/",blank=True,null=True)
    r_license = models.ImageField(upload_to="restaurant/license",blank=True,null=True)

    class Meta:
        db_table= "restaurants"

    def __str__(self):
        return self.r_name






