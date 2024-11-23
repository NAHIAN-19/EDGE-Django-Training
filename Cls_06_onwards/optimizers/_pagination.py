from django.core.paginator import Paginator
# Using  Paginator 
items = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
paginator = Paginator(items, 3)
page1 = paginator.page(1)
print(page1.object_list)