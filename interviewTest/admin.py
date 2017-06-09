# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from interviewTest.models import ClientAccount, OtherInformation

admin.site.register(ClientAccount)
admin.site.register(OtherInformation)