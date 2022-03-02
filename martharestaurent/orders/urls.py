from unicodedata import name
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.order_form, name="placeorder"),
    path('details/', views.more_info, name='moreinfo')
]