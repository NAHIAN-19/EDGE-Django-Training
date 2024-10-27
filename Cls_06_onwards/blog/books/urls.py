from books.views import (APIAuthor, APIBook, APIPublisher, BookAddView,
                        BookListView, ContactFormView, MyView)
from django.shortcuts import render
from django.urls import path

urlpatterns = [
    # Initial class based view urls
    path('initial_class/', MyView.as_view(), name='initial_class'),
    
    # Books related urls
    path('add/', BookAddView.as_view(), name='book_add'),
    path('list/', BookListView.as_view(), name='book_list'),
    
    # Contact form related urls
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('contact_success/', lambda request: render(request,'success/contact_success.html'), name='contact_success'),
    
    # Rest api urls
    path('api/books/', APIBook.as_view(), name='api_books'), # Book List and Create
    path('api/books/<int:pk>/', APIBook.as_view(), name='api_book'), # Book Retrieve, Update and Delete
    path('api/authors/', APIAuthor.as_view(), name='api_authors'), # Author List and Create
    path('api/authors/<int:pk>/', APIAuthor.as_view(), name='api_author'), # Author Retrieve, Update and Delete
    path('api/publishers/', APIPublisher.as_view(), name='api_publishers'), # Publisher List and Create
    path('api/publishers/<int:pk>/', APIPublisher.as_view(), name='api_publisher'), # Publisher Retrieve, Update and Delete
]
