from django.shortcuts import render
from django.contrib import messages
from .models import Author

def show_author_details(request):
    author_info = Author.objects.all()
    if request.method == 'POST':
        author_name = request.POST.get('author_name')
        author_birth_date = request.POST.get('author_birth_date')
        if author_birth_date == '':
            author_birth_date = '2021-01-01'
        author = Author(name=author_name, birth_date=author_birth_date)
        author.save()
        
        messages.success(request, 'Author Info added successfully')
    author_info = Author.objects.all()
    return render(request, 'hello.html', {'author_info': author_info})


# python generator, threading, asyn, syn
# New function before __init__
# Q, F, Sum, Count, Avg, Prefetch(for many to many), select_related(for one to many)