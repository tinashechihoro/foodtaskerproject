from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth

from foodtaskerapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^restaurant/sign-in/$', auth.login,
        {'template_name':'restaurant/sign_in.html'},
        name='restaurant-sign-in'),
    url(r'^restaurant/sign-out',auth.logout,
        {'next_page':'/'},
        name='restaurant-sign-out')
]
