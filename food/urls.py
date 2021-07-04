from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.fooditem,name="fooditem"),
    path('menu/',views.foodMenu),
    path('rest_home/',views.resthome),
    path('order/',views.order),
    path('verifyEmail/',views.verifyEmail),
    path('cart/',views.cart,name="cart"),
    path('cart/delete',views.cartDelete,name="cart"),
    path('item/delete',views.itemDelete,name="cart"),
    path('individual/',views.individual),

]