from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('Hello/', views.Hello, name='Hello'),
    path('bookstore/', views.bookstore, name='bookstore'),
    path('bookstore/detail/<int:id>',views.detail,name='detail'),
    path('contact/',views.contact,name='contact'),
    path('add_newbook/',views.add_newbook,name='add_newbook'),
    path('bookstore/detail/update/<int:id>',views.update,name='update'),
    path('bookstore/detail/delete/<int:id>',views.delete,name="delete"),
    path('bookstore/detail/availabel/<int:id>',views.delete,name="availabel"),
]

