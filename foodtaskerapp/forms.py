from django import forms

from django.contrib.auth.models import User

from foodtaskerapp.models import Restaurant

class UserForm(forms.ModelForm):
    """UserForm form"""
    class Meta:
        model = User
        fields = ('username','pasword','first_name','last_name','email')


class RestaurantForm(forms.ModelForm):
    """RestaurantForm form"""
    class Meta:
        model = Restaurant
        fields = ('name','phone','adddres','logo')
