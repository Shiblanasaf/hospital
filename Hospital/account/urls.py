from django.urls import path
from .views import loginview
from .views import registerview

urlpatterns=[
    path('login',loginview,name='log'),
    path('register',registerview,name='reg')
]