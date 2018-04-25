# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from foodtaskerapp.models import Restaurant,Driver,Customer

admin.site.register(Restaurant)
admin.site.register(Driver)
admin.site.register(Customer)
