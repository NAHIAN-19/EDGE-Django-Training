from django.shortcuts import render

def hello_blog(request):
    return render(request, 'hello.html')