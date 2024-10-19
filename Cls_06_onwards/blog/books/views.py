from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'hello.html'
    context_object_name = 'books'
    
    def get_queryset(self):
        return Book.objects.all().order_by('title')
    
# python generator, threading, asyn, syn, DRY, WAIT, KISS, 
# New function before __init__
# Q, F, Sum, Count, Avg, Prefetch(for many to many), select_related(for one to many)
# Https status code
# from django.views import View
# from django.http import HttpResponse

# class MyView(View):
#     def get(self, request):
#         return HttpResponse('Welcome to Django from Class!')