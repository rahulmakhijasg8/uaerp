from django.urls import path
from .import views

urlpatterns = [
    path('', views.login_user, name = 'login'),
    path('data_list', views.dataList, name = 'datalist'),
    path('homef/', views.a, name = 'a'),
    path('b/', views.b, name = 'b'),
    path('b/b/d/<int:id>/', views.d, name = 'd'),
    path('b/b/d/<int:id>/payments', views.e, name = 'e'),
    path('b/b/d/<int:id>/addguests', views.f, name = 'f'),
    path('b/b/d/<int:id>/addhotels', views.g, name = 'g'),
    path('b/b/d/<int:id>/addtransport', views.h, name = 'h'),
    path('b/b/d/<int:id>/addactivities', views.i, name = 'i'),
    path('delete/', views.delete, name = 'delete'),
    path('edit/', views.edit, name = 'edit'),
    path('index/',views.index,name='index'),
    path('tdelete/', views.tdelete, name = 'tdelete'),
    path('tedit/', views.tedit, name = 'tedit'),
    path('adelete/', views.adelete, name = 'adelete'),
    path('aedit/', views.aedit, name = 'aedit'),
    path('b/b/d/<int:id>/<int:hid>/hpayments/', views.hotel_payments, name = 'hpayments'),
    path('b/b/d/<int:id>/<int:tid>/tpayments/', views.transport_payments, name = 'tpayments'),
    path('b/b/d/<int:id>/<int:aid>/apayments/', views.activity_payments, name = 'apayments'),
]