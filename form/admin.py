from django.contrib import admin
from django.contrib.admin.decorators import register
from django.shortcuts import render
from .models import Connections, EntryForm, Bookinginfo, PersonalInfo, Hotelinfo,Paymentinfo,Activitiesinfo, Transportinfo

admin.site.register(EntryForm)
admin.site.register(Bookinginfo)
admin.site.register(PersonalInfo)
admin.site.register(Hotelinfo)
admin.site.register(Paymentinfo)
admin.site.register(Connections)
admin.site.register(Activitiesinfo)
admin.site.register(Transportinfo)