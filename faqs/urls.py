from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_and_add_faqs, name='faqs')
]
