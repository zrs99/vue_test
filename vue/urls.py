
from django.contrib import admin
from django.urls import path

# from django.conf.urls import

from django.urls import path, include
# from .views import add_book, show_books
from .views import add_book, show_books

urlpatterns = [
    path("add_book",  add_book),
    path("show_books", show_books ),
]
