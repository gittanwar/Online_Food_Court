from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import OrderForm
from .models import Food_items, Cart
import smtplib


class ChechOut:
    def __init__(self, Sno, Image, Product, Price, Quantity, subTotal):
        self.sno = Sno
        self.image = Image
        self.product = Product
        self.price = Price
        self.quantity = Quantity
        self.subTotal = subTotal


# Create your views here.
def fooditem(request):
    #      r_mobile = request.session['r_mobile']
    #      allItems = Food_items.objects.filter(restaurant=r_mobile)
    #      if request.method == 'POST':
    #          form = FoodForm(request.POST, request.FILES)
    #          if form.is_valid():
    #              form.save()
    #              allItems.add(form)
    #          else:
    #              return HttpResponse("Form not valid {}".format(form))
    #      else:
    #          form = FoodForm()
    #      print(allItems)
    #      return render(request, "food/foodhome.html",{"f": form, 'items': allItems,"MM":r_mobile})
    r_mobile = request.session['r_mobile']
    allitems = Food_items.objects.filter(restaurant=r_mobile)
    # allitems=Food_items.objects.all()
    return render(request, 'food/foodhome.html', {'items': allitems})


def foodMenu(request):
    if request.method == 'POST':
        cart = Cart()
        cart.item_id = request.POST['item_id']
        cart.count = request.POST['item_count']
        cart.save()
    allitems = Food_items.objects.all()
    return render(request, 'food/foodhome.html', {'items': allitems})


def individual(request):
    allitems = Food_items.objects.filter(restaurant=request.GET['rest'])
    # allitems=Food_items.objects.all()
    return render(request, 'food/foodhome.html', {'items': allitems})


def cart(request):
    cartList = Cart.objects.all()
    checkOutList = list()
    sno = 0
    total = 0

    for item in cartList:
        sno += 1
        food = Food_items.objects.get(id=item.item_id)

        subTotal = item.count * food.price
        total += subTotal
        checkOut = ChechOut(Sno=item.id, Image=food.food_image, Product=food.name, Price=food.price,
                            Quantity=item.count,
                            subTotal=subTotal)

        checkOutList.append(checkOut)
    form = OrderForm()
    return render(request, "food/cart.html", {"checkOutList": checkOutList, "total": total, 'form': form})


def cartDelete(request):
    sno = request.GET['sno']
    Cart.objects.get(id=sno).delete()

    return redirect("/food/cart")

def itemDelete(request):
    sno = request.GET['sno']
    Food_items.objects.get(id=sno).delete()

    return redirect("/food/rest_home")


def saveOrder(request):
    form = OrderForm(request.POST)
    if form.is_valid():
        form.save()

        return render(request, "restaurant/orderVerify.html", )
    else:
        return HttpResponse("Details are missing {}".format(form))


def verifyEmail(request):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    # Authentication
    s.login("dheerajtanwar129@gmail.com", "dheeraj129@")

    # message to be sent
    message = 'this email is for Online food court verification.' \
              ' Click link to verify your order. {}'.format(request)

    # sending the mail
    s.sendmail("dheerajtanwar129@gmail.com", "sr2081999@gmail.com", message)

    # terminating the session
    s.quit()
    return HttpResponse("We have sent an email to your account. Please open email in next tab and click the link")


def order(request):
    return render(request, "order/orderhome.html", )


def resthome(request):
    r_mobile = request.session['r_mobile']
    allitems = Food_items.objects.filter(restaurant=r_mobile)
    return render(request, "restaurant/rest_dashboard.html", context={'f': allitems})