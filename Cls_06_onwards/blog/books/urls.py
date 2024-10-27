from books import views
from django.urls import path
from django.shortcuts import render

urlpatterns = [
    # Initial class based view urls
    path('initial_class/', views.MyView.as_view(), name='initial_class'),
    # Books related urls
    path('add/', views.BookAddView.as_view(), name='book_add'),
    path('list/', views.BookListView.as_view(), name='book_list'),
    # Contact form related urls
    path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('contact_success/', lambda request: render(request,'success/contact_success.html'), name='contact_success'),
]
