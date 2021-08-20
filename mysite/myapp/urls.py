from django.contrib import admin
from django.urls import path
from myapp import views


app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('book/<int:book_id>/', views.detail, name='detail'),
    path('add/', views.add_book, name='add_book'),
    path('update/<int:book_id>/', views.update, name='update'),
    path('delete/<int:book_id>/', views.delete, name='delete'),
]
