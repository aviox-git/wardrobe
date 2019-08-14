# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import binascii
import os
from django.contrib.auth.models import User
# Create your models here.

class AppToken(models.Model):

    app_version = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add = True)
    device_type = models.CharField(max_length=100)
    device_id = models.CharField(max_length=100)
    key = models.CharField(max_length=100,blank = True)

    def __str__(self):
        return self.key + " : " + self.device_type

    def save(self, *args, **kwargs):
        self.key = binascii.hexlify(os.urandom(20)).decode()
        return super(AppToken, self).save(*args, **kwargs)

Gender = (("M", "Male"),("F", "Female"),("O","Other"))
class UserModel(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	phone = models.PositiveIntegerField(blank=True,null=True,default=None)
	image = models.ImageField(upload_to = 'profile',blank=True,null=True)
	dob = models.DateField(verbose_name='Date of Birth')
	gender = models.CharField(max_length = 1, choices = Gender)

	def __str__(self):
		return self.user.username + " : " + self.gender

class CategoryModel(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.user.username + " : " + self.name
