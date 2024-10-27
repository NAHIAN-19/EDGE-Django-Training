from .models import Book
from .forms import ContactForm, BookForm
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, FormView, CreateView
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.mixins import PermissionRequiredMixin
    
# Introduction to Class based view
class MyView(View):
    # Get method to show http response using 2 arguments 
    def get(self, request):
        return HttpResponse('Welcome to Django from Class!')    

# Class based view using form validation
class ContactFormView(FormView):
    # Template name to render the form
    template_name = 'contact.html'
    # Form class to validate the form
    form_class = ContactForm
    # Success url to redirect after form submission
    success_url = reverse_lazy('contact_success')
    # Show http response after form validation
    def form_valid(self, form) -> HttpResponse:
        return super().form_valid(form)
    
# Add New Book details using Model form validation
class BookAddView(PermissionRequiredMixin, CreateView): 
    model = Book                                # Model name to add new book details   
    form_class = BookForm                       # Form class to validate the form
    template_name = 'books/books_add.html'      # Template name to render the form
    success_url = reverse_lazy('book_list')     # Success url to redirect after form submission
    permission_required = 'books.can_add_books' # Permission required to add new book details
    
    def handle_no_permission(self):
        """
            To add permission to user:
            from django.contrib.auth.models import Permission, User
            user = User.objects.get(username="nahian")
            permission = Permission.objects.get(codename="can_add_books")
            user.user_permissions.add(permission)
        """
        return HttpResponseForbidden("You do not have permission to add a book.")
    # Show http response after form validation
    def form_valid(self, form) -> HttpResponse:
        return super().form_valid(form)
    

# Return All Book details
class BookListView(ListView):
    model = Book                            # Model name to show all book details                
    template_name = 'books/books_list.html' # Template name to render the form
    
    # context to use the objects of Book model in template
    context_object_name = 'books'    
    




# python generator, threading, asyn, syn, DRY, WAIT, KISS, 
# New function before __init__
# Q, F, Sum, Count, Avg, Prefetch(for many to many), select_related(for one to many)
# Https status code
# Html template tags
