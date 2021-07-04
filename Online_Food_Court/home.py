from django.shortcuts import render
from restaurant.models import Restaurant
def home(request):
    allRest=Restaurant.objects.all()


    return render(request,template_name="homepage.html",context={"rests":allRest})