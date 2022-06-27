from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST

from accounts.models import User
from courses.models import Course
from home.models import Enroll
from .cart import Cart


@require_POST
def cart_add(request, slug):
    cart = Cart(request)  # create a new cart object passing it the request object
    course = get_object_or_404(Course, slug=slug)
    cart.add(course=course, quantity=1, update_quantity=False)
    return redirect('cart:cart_detail')


def course_cart_add(request, id):
    cart = Cart(request)
    course = get_object_or_404(Course, id=id)
    cart.add(course=course, quantity=1, update_quantity=False)
    return redirect('cart:cart_detail')


def cart_remove(request, slug):
    cart = Cart(request)
    course = get_object_or_404(Course, slug=slug)
    cart.remove(course)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})


@login_required(login_url='/login')
def cart_checkout(request):
    carts = Cart(request)
    total_price = 0
    for cart in carts:
        course = cart['course']
        total_price = total_price + course.price
        Enroll.objects.create(course=course, user_id=request.user.id)

    print(total_price)

    messages.success(request, 'Successfully checked out!')
    # carts.clear()
    return redirect(reverse_lazy('cart:cart_detail'))
