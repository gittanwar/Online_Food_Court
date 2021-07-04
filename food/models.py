from django.db import models

# Create your models here.
class Food_items(models.Model):
    name = models.CharField("Food Name", max_length=100)
    price = models.IntegerField()
    restaurant = models.IntegerField()
    food_image = models.ImageField(upload_to='FOOD')

    class Meta:
        db_table = "food_items"

    def __str__(self):
        return self.name


class Cart(models.Model):
    item_id = models.IntegerField()
    count = models.IntegerField()



# Create your models here.
class Order(models.Model):
    u_name = models.CharField(max_length=30)
    email = models.CharField(max_length=35)
    ph_no = models.IntegerField()
    state = models.CharField(max_length=20)
    pin_code = models.IntegerField()
    address = models.CharField(max_length=60)

    class Meta:
        db_table = "order"

    def __str__(self):
        return self.order_id