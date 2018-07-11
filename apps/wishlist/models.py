# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from datetime import datetime, date
from django.db import models



class UserManager(models.Manager):
    def register_validate(self, postData):
        errors = []


        name = postData['name']
        username = postData['username']
        password = postData['password']
        cpassword = postData['cpassword']
        hireddate = postData['hireddate']

        if not name or not username or not password or not cpassword:
            errors.append( "All fields are required")

        # check name
        if len(name) < 3 :
            errors.append( "name fields should be at least 3 characters")

        # check username
        if len(username)<0:
            errors.append('please enter a username')

        # check password
        if len(password ) < 8:
            errors.append ( "password must be at least 8 characters")
        elif password != cpassword:
            errors.append ( "password must be match")

        if not errors:
            if User.objects.filter(username=username):
                errors.append("username is not unique")
            else:
                hashed = bcrypt.hashpw((password.encode()), bcrypt.gensalt(5))

                return self.create(

                    name = name,
                    username= username,
                    hireddate= hireddate,
                    password= hashed
                )

        return errors

    def login_validate(self, postData):
        errors = []
        password = postData['password']
        username = postData['username']
                # check DB for email
        try:
            # check user's password and username
            if len(self.filter(username=username)) > 0:
                user = self.filter(username=username)[0]
            # user = self.get(username=username)
            if bcrypt.checkpw(password.encode(), user.password.encode()):
                return user

        except:
            pass

        errors.append('Invalid login info')
        return errors

class WishManager(models.Manager):
    def item_validate(self, postData, id):
        errors = []
        item = postData['item']
        # check item
        if not item:
            errors.append( "Item field are required")
        elif len(item) < 3 :
            errors.append( "item field should be at least 3 characters")
        if not errors:
            user = User.objects.get(id=id)
            item = self.create(

                    item = item,
                    created_by = user # one to many (ForeignKey) must be inside of self.creation---> can't be null
                )
            item.wished_by.add(user)
            return item

        return errors




class User(models.Model):
      name = models.CharField(max_length=255, default="")
      username = models.CharField(max_length=255)
      password = models.CharField(max_length=255)
      hireddate = models.CharField(max_length=100, default=0)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      objects = UserManager()

class ItemWish(models.Model):
    item = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, related_name="items_added")# "created_by" logged user
    wished_by = models.ManyToManyField(User, related_name = "wishes") # "wished_by" all the users
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = WishManager()

    # ItemWish.created_by ---->  user created that wish
    # ItemWish.wished_by ------> all the users who have wished
    # User.items_added -------->items added by the that user
    # User. wishes --------> all the users wishes
