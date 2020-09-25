from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required

from App_Order.models import Cart,Order
from App_Shop.models import Product

from django.contrib import messages

@login_required
def add_to_cart(request,pk):
    item = get_object_or_404(Product,pk=pk)
    print("item :"+str(item))
    # this will also make a list if the product is selected before
    # idexing
    order_item = Cart.objects.get_or_create(item=item,user=request.user,purchased=False)
    print("order Item :"+str(order_item))
    # get the order object that is yet not paid
    # and try to add the cart in it
    # other wise create it
    # it will return a list even it is only one
    # so make indexing
    order_qs = Order.objects.filter(user=request.user,ordered=False)

    ## chek if you even create any unpaid order yet
    if order_qs.exists():
        order = order_qs[0]
        print("Order Exists adding to it")
        print(order)
        if order.orderitems.filter(item=item).exists():
            # the product exists in the order
            # so increase the cart
            # orderitem[0] is the cart that is matched because it return a list even
            # it is only one element
            # we checked all the cart in a order to seach the duplicate
            # then increase it
            # we are increasing the cart
            order_item[0].quantity +=1
            order_item[0].save()
            messages.info(request,"This Item Quantity was updated")
            return redirect("App_Shop:home")
