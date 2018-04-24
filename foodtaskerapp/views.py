# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/restaurant/sign-in/')
def home(request):
    """home page"""
    return redirect(restaurant_home)

def restaurant_home(request):
    """restaurant_home"""
    return  render(request,'restaurant/home.html',{})
def restaurant_sign_up(request):
    """restaurant_sign_up view"""
    return render(request,'restaurant/sign_up.html',{})