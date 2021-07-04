from django.forms import ModelForm

from .models import Food_items, Order


class FoodForm(ModelForm):
    class Meta:
        model = Food_items
        fields = "__all__"


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
