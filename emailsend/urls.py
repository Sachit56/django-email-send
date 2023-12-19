from django.urls import path
from . import views

app_name='emailsend'

urlpatterns = [
    path('',views.EmailView,name='email')
]
