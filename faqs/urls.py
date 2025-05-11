from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_and_add_faqs, name='faqs'),
    path('edit/<int:faq_id>/',
         views.edit_faq, name='edit_faq'),
    path('delete/<int:faq_id>/',
         views.delete_faq, name='delete_faq'),
]
