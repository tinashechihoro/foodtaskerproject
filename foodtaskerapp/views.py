# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def home(request):
    """homa page"""
    return render(request,'home.html',{})
