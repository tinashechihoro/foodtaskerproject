# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def home(request):
    """home page"""
    return render(request,'home.html',{})

def restaurant_home(request):
    """restaurant_home"""
    return  render(request,'restaurant/home.html',{})