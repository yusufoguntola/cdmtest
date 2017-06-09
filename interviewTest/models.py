# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ('Male','Male'),
    ('Female','Female'),
)

ACCOUNT_STATUS = (
    ('Pending','Pending'),
    ('Approved','Approved'),
    ('Rejected','Rejected'),
)


class ClientAccount(models.Model):
    user = models.OneToOneField(User)
    client_id = models.CharField(max_length=15, db_index=True)
    DOB = models.DateField(null=True)
    gender = models.CharField(max_length=8, null=True)
    status = models.CharField(max_length=8, choices=ACCOUNT_STATUS, default='Pending')
    is_approved = models.BooleanField(default=False)
    signup_complete = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.client_id


class OtherInformation(models.Model):
    client = models.OneToOneField(ClientAccount)
    home_address = models.CharField(max_length=20)
    place_of_birth = models.CharField(max_length=20)
    occupation = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.client.client_id