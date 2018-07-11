# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User
from .models import ItemWish
from django.contrib import messages

#==================================================#
#                  RENDER METHODS                  #
#==================================================#

def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, "wishlist/index.html", context)


def dashboard(request):

    try:
        context = {
            'user': User.objects.get(id=request.session['user_id']),

            'my_wishes':ItemWish.objects.filter(wished_by=request.session['user_id']),

            'other_wishes': ItemWish.objects.exclude(wished_by=request.session['user_id']),

        }
        return render (request, "wishlist/dashboard.html", context)

    except KeyError:
        return redirect('/')

def add(request):

    return render(request, 'wishlist/new.html')

def show(request, id):
    context={
        'item':ItemWish.objects.get(id=id)
    }
    return render (request, "wishlist/show.html", context)



#==================================================#
#                 PROCESS METHODS                  #
#==================================================#

def register(request):
    result = User.objects.register_validate(request.POST)
    if type(result) == list:
        for error in result:
            messages.error(request, error)
        return redirect('/')

    request.session['user_id'] = result.id
    # messages.success(request, "Successfully registered!")
    return redirect('/dashboard')


def login(request):
    result = User.objects.login_validate(request.POST)
    if type(result) == list:
        for error in result:
            messages.error(request, error)
        return redirect ("/")

    request.session['user_id'] = result.id
    # messages.success(request, "Successfully logged in!")
    return redirect("/dashboard")

def logout(request):
    request.session.clear()
    return redirect ("/")

def create(request):
    result = ItemWish.objects.item_validate(request.POST, request.session['user_id'])
    if type(result) == list:
        for error in result:
            messages.error(request, error)
        return redirect ("/")
    return redirect('/dashboard')

def delete(request, id):
    item = ItemWish.objects.get(id=id)
    item.delete()
    return redirect ('/dashboard')

def remove(request, id):
    items_added = ItemWish.objects.get(id=id)
    user=User.objects.get(id=request.session['user_id'])
    user.wishes.remove(items_added)
    return redirect ('/dashboard')

def join(request, id): # add to my wishlist
    other_wishes = ItemWish.objects.get(id=id)
    user=User.objects.get(id=request.session['user_id'])
    user.wishes.add(other_wishes)
    return redirect ('/dashboard')
