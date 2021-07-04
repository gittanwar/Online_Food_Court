from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Restaurant

# Create your views here.
from .forms import RestroForm


def home(request):
    if request.method == 'POST':
        form = RestroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        else:
            return HttpResponse("Form not valid {}".format(form))
    else:
        form = RestroForm()

    return render(request, "restaurant/restauranthome.html", context={'f': form})


def login(request):
    if request.method == 'POST':
        r_mobile = request.POST['restro']
        password = request.POST['pass']

        resturant = Restaurant.objects.get(r_mobile=r_mobile)

        if resturant.r_pass == password:
            request.session['r_mobile'] = r_mobile
            return redirect("/food/rest_home")
        else:
            return HttpResponse("Login failed")

    return HttpResponse('Params not confirmed')
