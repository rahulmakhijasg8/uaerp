from django.urls import path
from .import views

urlpatterns = [
    path('', views.login_user, name = 'login'),
    path('data_list', views.dataList, name = 'datalist'),
    path('a/', views.a, name = 'a'),
    path('b/', views.b, name = 'b'),
    path('b/b/d/<int:id>/', views.d, name = 'd'),
    path('b/b/d/<int:id>/b/d//e', views.e, name = 'e'),
    path('b/b/d/<int:id>/b/d//e/f', views.f, name = 'f'),
    path('b/b/d/<int:id>/b/d//e/f/g', views.g, name = 'g'),
    path('b/b/d/<int:id>/b/d//e/f/g/h', views.h, name = 'h'),
    path('b/b/d/<int:id>/b/d//e/f/g/h/i', views.i, name = 'i'),
    path('delete/', views.delete, name = 'delete'),
    path('edit/', views.edit, name = 'edit'),
    path('index/',views.index,name='index'),
     path('b/b/d/<int:id>/<int:hid>/hpayments', views.hotel_payments, name = 'hpayments'),
]