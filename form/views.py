from django import forms
from django.db import connections
from django.db.models import Q
from django.db.models.aggregates import Sum
from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import *
from .models import Activitiesinfo, EntryForm, Hotelinfo, PersonalInfo, Bookinginfo,Paymentinfo,Connections, Transportinfo
from .filters import DataFilter
import json
import random, string
from django.conf import settings
from django.core.mail import send_mail , EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
import os



def Entryform(request):
    form = entryForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = entryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return render(request,'entryform.html',{'form':form})

def dataList(request):
    Entryform = EntryForm.objects.all()
    myFilter = DataFilter(request.GET, queryset=Entryform)
    Entryform = myFilter.qs
    return render (request,'datalist.html',{'Entryform':Entryform,'myFilter':myFilter})

def a(request):
     if request.method == 'POST':
        name=request.POST.get('Name')
        phoneno = request.POST.get('Phone')
        email = request.POST.get('Email')
        dob = request.POST.get('dob')
        sex = request.POST.get('Sex')
        occupation = request.POST.get('Occupation')
        address = request.POST.get('Address')
        city = request.POST.get('City')
        state = request.POST.get('State')
        aadhar = request.POST.get('Aadhar')
        personalinfo = PersonalInfo.objects.create(Name = name,PhoneNo = phoneno,Email = email,DOB = dob,Gender = sex, 
                                                    Occupation = occupation, Address = address, City = city,
                                                     State = state, Aadhar_Card_No = aadhar )
        
        tripname = request.POST.get('TripName')
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')
        tcity = request.POST.get('Tripcity')
        tstate = request.POST.get('Tripstate')
        service = request.POST.get('cbox')
        totalcost = request.POST.get('totalcost')
        amountpaid = request.POST.get('amountpaid')
        dueamount = request.POST.get('dueamount')
        paymentdate = request.POST.get('payment-date')
        modeofpayment = request.POST.get('modeofpayment')
        additionalinfo = request.POST.get('additionalinfo')
        createdby = request.POST.get('createdby')
        duedate = request.POST.get('duedate')
        servicestatus = request.POST.get('status')
        noofpeople = request.POST.get('noofpeople')
        bookinginfo=Bookinginfo.objects.create(Bookingkey = x, personal_details = personalinfo, Trip_Name=tripname,Start_Date=startdate,
                                    End_Date=enddate,City=tcity, State=tstate,Service=service,Total_Cost=totalcost,Amount_Paid=amountpaid,
                                    Due_amount=dueamount,BookingDate=paymentdate,Mode_of_payment=modeofpayment,Additional_info=additionalinfo,
                                    Created_by=createdby,Due_Date=duedate,Service_Status=servicestatus,No_of_People=noofpeople)

        Connections.objects.create(Bookingkey=bookinginfo,Membertype = 'Prime',Personalkey=personalinfo )

        payment = Paymentinfo.objects.create(Bookingkey=bookinginfo,Payment_Type='Customer',Amount=amountpaid,Date=paymentdate,
                                    Mode_of_payment=modeofpayment,Additional_info=additionalinfo)
     
     return render(request, "c.html")




  
x = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(11))





def b(request):
    Entryform = Bookinginfo.objects.all()
    myFilter = DataFilter(request.GET, queryset=Entryform)
    Entryform = myFilter.qs
    return render (request,'b.html',{'Entryform':Entryform,'myFilter':myFilter})
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

@csrf_exempt
def d(request,id):
    id = id
    a = Bookinginfo.objects.get(id=id)
    b = Paymentinfo.objects.filter(Bookingkey=id).all()
    amtpaid =Paymentinfo.objects.filter(Bookingkey=id,Payment_Type='Customer').aggregate(Sum('Amount'))
    Bookinginfo.objects.filter(id=id).update(Amount_Paid=amtpaid['Amount__sum'])
    pinfo = PersonalInfo.objects.filter(connections__Bookingkey=id)
    transport = Transportinfo.objects.filter(Bookingkey=id).all()
    activity = Activitiesinfo.objects.filter(Bookingkey=id).all()
    d = Hotelinfo.objects.filter(Bookingkey=id).all()
    if request.method == 'POST':

        name = request.POST['Tripname']
        city = request.POST['Tripcity']
        createdby = request.POST['Createdby']
        startdate = request.POST['Startdate']
        enddate = request.POST['Enddate']
        noofpeople = request.POST['Noofpersons']
        additionalinfo = request.POST['Additionalinfo']
        totalcost = request.POST['Totalcost']
        amountpaid = request.POST['Amountpaid']
        dueamount = request.POST['dueamount']
        duedate = request.POST['Duedate']
        date = datetime.strptime(startdate, '%b. %d, %Y').date()
        edate = datetime.strptime(enddate, '%b. %d, %Y').date()
        ddate = datetime.strptime(duedate, '%b. %d, %Y').date()
        bookinginfo=Bookinginfo.objects.get(id=id)

        
        bookinginfo.Trip_Name=name
        bookinginfo.City = city
        bookinginfo.Created_by = createdby
        bookinginfo.Start_Date = date
        bookinginfo.End_Date = edate
        bookinginfo.No_of_People = noofpeople
        bookinginfo.Additional_info = additionalinfo
        bookinginfo.Total_Cost = totalcost
        bookinginfo.Amount_Paid = amountpaid
        bookinginfo.Due_amount = dueamount 
        bookinginfo.Due_Date = ddate
        bookinginfo.save()

        
        

       
        return render(request, 'd.html',{'id':id,'a':bookinginfo,'b':b,'c':pinfo,'d':d,'transport':transport,'activity':activity,'amtpaid':amtpaid['Amount__sum']})
    return render(request, 'd.html',{'id':id,'a':a,'b':b,'c':pinfo,'d':d,'transport':transport,'activity':activity,'amtpaid':amtpaid['Amount__sum']})

def e(request,id):
    id=id
    bookinginfo = Bookinginfo.objects.get(id=id)
    if request.method == 'POST':
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        mode = request.POST.get('mode')
        info = request.POST.get('info')

        Paymentinfo.objects.create(Bookingkey=bookinginfo,Payment_Type='Customer',Amount=amount,Date=date,
                                    Mode_of_payment=mode,Additional_info=info)
        amtpaid =Paymentinfo.objects.filter(Bookingkey=id,Payment_Type='Customer').aggregate(Sum('Amount'))
        Bookinginfo.objects.filter(id=id).update(Amount_Paid=amtpaid['Amount__sum'])
        tcost =Bookinginfo.objects.filter(id=id).values_list('Total_Cost', flat=True)[0]
        Bookinginfo.objects.filter(id=id).update(Due_amount=tcost-amtpaid['Amount__sum'])
    return render(request, 'f.html',{'id':id})

def f(request,id):
    id=id
    bookinginfo = Bookinginfo.objects.get(id=id)
    if request.method == 'POST':
        name=request.POST.get('Name')
        phoneno = request.POST.get('Phone')
        email = request.POST.get('Email')
        dob = request.POST.get('dob')
        sex = request.POST.get('Sex')
        occupation = request.POST.get('Occupation')
        address = request.POST.get('Address')
        city = request.POST.get('City')
        state = request.POST.get('State')
        aadhar = request.POST.get('Aadhar')
        
        persnalinfo = PersonalInfo.objects.create(Name = name,PhoneNo = phoneno,Email = email,DOB = dob,Gender = sex, 
                                                    Occupation = occupation, Address = address, City = city,
                                                     State = state, Aadhar_Card_No = aadhar )
        connections = Connections.objects.create(Bookingkey=bookinginfo,Personalkey = persnalinfo, Membertype = 'NotPrime')
    return render(request, 'e.html',{'id':id})

from django.core import serializers
from .serializers import Hotelinfoserializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def g(request,id):
    id=id
    bookinginfo = Bookinginfo.objects.get(id=id)
    if request.method == 'POST':
        hotelename=request.POST.get('Hotelname')
        hotelcity = request.POST.get('Hotelcity')
        hotelstate = request.POST.get('Hotelstate')
        checkin = request.POST.get('Checkindate')
        checkout = request.POST.get('Checkoutdate')
        rooms = request.POST.get('Rooms')
        roomsharing = request.POST.get('Roomsharing')
        roomtype = request.POST.get('Roomtype')
        mealplan = request.POST.get('Mealplan')
        addinfo = request.POST.get('Additionalinfo')
        roomcost = request.POST.get('Roomcost')
        hname = request.POST.get('Name')
        hnumber = request.POST.get('Number')
        hemail = request.POST.get('Email')
        hadditionalinfo = request.POST.get('Additionalinfo')

        hid = request.POST['hiid']
        hotelcity = request.POST['Hotelcity']
        hotelstate = request.POST['Hotelstate']
        checkin = request.POST['Checkindate']
        checkout = request.POST['Checkoutdate']
        rooms = request.POST['Rooms']
        roomsharing = request.POST['Roomsharing']
        roomtype = request.POST['Roomtype']
        mealplan = request.POST['Mealplan']
        addinfo = request.POST['Additionalinfo']
        roomcost = request.POST['Roomcost']
        hname = request.POST['Name']
        hnumber = request.POST['Number']
        hemail = request.POST['Email']
        hadditionalinfo = request.POST['Additionalinfo']
        hoelname=request.POST['Hname']

        if hid =='':
            
            hotelinfo = Hotelinfo.objects.create(Bookingkey=bookinginfo,Hname=hoelname,Hstate=hotelstate,
                                                Hcity=hotelcity,Checkin_Date=checkin,Checktout_Date=checkout,
                                                No_of_rooms=rooms,Room_Type=roomtype,Meal_Plan=mealplan,
                                                Room_Sharing_Option=roomsharing,Total_Cost=roomcost,Hotel_Contact_Name=hname,
                                                Hotel_Contact_No=hnumber,Hemail=hemail,Additional_info=hadditionalinfo,
                                                )
        else:
            Hotelinfo.objects.filter(id=hid).update(Bookingkey=bookinginfo,Hname=hoelname,Hstate=hotelstate,
                                             Hcity=hotelcity,Checkin_Date=checkin,Checktout_Date=checkout,
                                            No_of_rooms=rooms,Room_Type=roomtype,Meal_Plan=mealplan,
                                            Room_Sharing_Option=roomsharing,Total_Cost=roomcost,Hotel_Contact_Name=hname,
                                            Hotel_Contact_No=hnumber,Hemail=hemail,Additional_info=hadditionalinfo,
                                            )

       
       
        hinfo = Hotelinfo.objects.filter(Bookingkey=id).values()
        info = list(hinfo)
        #print(info)
        # hotelinfoserializer = Hotelinfoserializer(hotelinfo)
        # print(hotelinfoserializer.data)
        return Response({'status':'save', 'info':info})
    return render(request,'g.html',{'id':id})

@api_view(['GET','POST'])
def h(request,id):
    id=id
    bookinginfo = Bookinginfo.objects.get(id=id)
    if request.method == 'POST':
        vname=request.POST.get('vname')
        Startdate = request.POST.get('Startdate')
        enddate = request.POST.get('Enddate')
        slocation = request.POST.get('Slocation')
        elocation = request.POST.get('Elocation')
        additionalinfo = request.POST.get('Additionalinfo')
        dname = request.POST.get('Dname')
        dnumber = request.POST.get('dno')
        totalcost = request.POST.get('totalcost')

        tid = request.POST['tiid']
        vname=request.POST['vname']
        Startdate = request.POST['Startdate']
        enddate = request.POST['enddate']
        slocation = request.POST['slocation']
        elocation = request.POST['elocation']
        additionalinfo = request.POST['vadditionalinfo']
        dname = request.POST['dname']
        dnumber = request.POST['dno']
        totalcost = request.POST['totalcost']
        amountpaid = request.POST['amountpaid']
        dueamount = request.POST['dueamount']

        if tid =='':

            transportinfo = Transportinfo.objects.create(Bookingkey=bookinginfo,Vehicle_Name=vname,Driver_Name=dname,
                                            Driver_Phone_No=dnumber,Start_Date=Startdate,End_date=enddate,
                                            Start_Location=slocation,End_Location=elocation,Additional_info=additionalinfo,
                                            Total_Cost=totalcost)

        else:
            Transportinfo.objects.filter(id=tid).update(Bookingkey=bookinginfo,Vehicle_Name=vname,Driver_Name=dname,
                                            Driver_Phone_No=dnumber,Start_Date=Startdate,End_date=enddate,
                                            Start_Location=slocation,End_Location=elocation,Additional_info=additionalinfo,
                                            Total_Cost=totalcost)
                    
        tinfo = Transportinfo.objects.filter(Bookingkey=id).values()
        info = list(tinfo)
        #print(info)
        # hotelinfoserializer = Hotelinfoserializer(hotelinfo)
        # print(hotelinfoserializer.data)
        return Response({'status':'save', 'info':info})
    return render(request, 'h.html',{'id':id})

@api_view(['GET','POST'])
def i(request,id):
    id=id
    bookinginfo = Bookinginfo.objects.get(id=id)
    if request.method == 'POST':
        aname=request.POST.get('Activityname')
        state = request.POST.get('State')
        city = request.POST.get('City')
        noofpersons = request.POST.get('Noofperson')
        date = request.POST.get('Date')
        additionalinfo = request.POST.get('Additionalinfo')
        vname = request.POST.get('Vname')
        vno = request.POST.get('Vno')
        totalcost = request.POST.get('totalcost')

        aid = request.POST['aiid']
        aname=request.POST['aname']
        state = request.POST['astate']
        city = request.POST['acity']
        noofpersons = request.POST['anoofpersons']
        date = request.POST['adate']
        additionalinfo = request.POST['aadditionalinfo']
        vname = request.POST['avname']
        vno = request.POST['vno']
        totalcost = request.POST['atotalcost']
        amountpaid = request.POST['aamountpaid']
        dueamount = request.POST['adueamount']

        if aid =='':

         activityinfo = Activitiesinfo.objects.create(Bookingkey=bookinginfo,Name_of_activity=aname,State=state,
                                            City=city,No_of_People=noofpersons,Date=date,
                                            Vendor_Name=vname,Vendor_Contact_No=vno,Additional_info=additionalinfo,
                                            Total_Cost=totalcost)
        else:
            Activitiesinfo.objects.filter(id=aid).update(Bookingkey=bookinginfo,Name_of_activity=aname,State=state,
                                            City=city,No_of_People=noofpersons,Date=date,
                                            Vendor_Name=vname,Vendor_Contact_No=vno,Additional_info=additionalinfo,
                                            Total_Cost=totalcost)
       
        ainfo = Activitiesinfo.objects.filter(Bookingkey=id).values()
        info = list(ainfo)
        #print(info)
        # hotelinfoserializer = Hotelinfoserializer(hotelinfo)
        # print(hotelinfoserializer.data)
        return Response({'status':'save', 'info':info})
    return render(request, 'i.html',{'id':id})


def delete(request):
    if request.method == "POST":
        id = request.POST['hid']
        print(id)
        hi = Hotelinfo.objects.get(pk=id)
        hi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})

def edit(request):
    if request.method == "POST":
        id = request.POST['hid']
        print(id)
        hi = Hotelinfo.objects.get(pk=id)
        hidata = {"id":hi.id,"Hname":hi.Hname,"Hcity":hi.Hcity,"Hstate":hi.Hstate,
                 "Checkin_Date":hi.Checkin_Date,"Checktout_Date":hi.Checktout_Date,"No_of_rooms":hi.No_of_rooms,
                   "Room_Type":hi.Room_Type,"Meal_Plan":hi.Meal_Plan,"Room_Sharing_Option":hi.Room_Sharing_Option,
                    "Hotel_Contact_Name":hi.Hotel_Contact_Name,"Hotel_Contact_No":hi.Hotel_Contact_No,"Hemail":hi.Hemail,
                    "Total_Cost":hi.Total_Cost,"Additional_info":hi.Additional_info}

        return JsonResponse(hidata)

def tedit(request):
    if request.method == "POST":
        id = request.POST['tid']
        print(id)
        ti = Transportinfo.objects.get(pk=id)
        tidata = {"id":ti.id,"Vehicle_Name":ti.Vehicle_Name,"Driver_Name":ti.Driver_Name,"Driver_Phone_No":ti.Driver_Phone_No,
                 "Start_Date":ti.Start_Date,"End_date":ti.End_date,"Start_Location":ti.Start_Location,
                   "End_Location":ti.End_Location,"Total_Cost":ti.Total_Cost,"Additional_info":ti.Additional_info}

        return JsonResponse(tidata)

def tdelete(request):
    if request.method == "POST":
        id = request.POST['tid']
        print(id)
        ti = Transportinfo.objects.get(pk=id)
        ti.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})

def aedit(request):
    if request.method == "POST":
        id = request.POST['aid']
        print(id)
        ai = Activitiesinfo.objects.get(pk=id)
        tidata = {"id":ai.id,"Name_of_activity":ai.Name_of_activity,"State":ai.State,"City":ai.City,
                 "No_of_People":ai.No_of_People,"Date":ai.Date,"Vendor_Name":ai.Vendor_Name,
                   "Vendor_Contact_No":ai.Vendor_Contact_No,"Total_Cost":ai.Total_Cost,"Additional_info":ai.Additional_info}

        return JsonResponse(tidata)

def adelete(request):
    if request.method == "POST":
        id = request.POST['aid']
        print(id)
        ai = Activitiesinfo.objects.get(pk=id)
        ai.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})



def index(request,id,pid):
  
  bookinginfo = Bookinginfo.objects.get(id=id)
  pinfo = PersonalInfo.objects.filter(connections__Bookingkey=id,connections__Membertype='Prime').get()
  payinfo = Paymentinfo.objects.filter(Bookingkey=id,id=pid).get()
  message_body = render_to_string('mail.html', {
            'bookinginfo':bookinginfo,'pinfo':pinfo,'payinfo':payinfo
        })
  mail = EmailMessage(
    subject='Payment Confirmation',
    body=message_body,
    from_email = 'booking@universaladventure.in',
    #from_email=settings.EMAIL_HOST_USER,
            to=[pinfo.Email])
  mail.content_subtype = "html"
  mail.send()
  messages.info(request,'mail sended successfully')
  return render(request,'index.html',{})


def hotel_payments(request,id,hid):
    id=id
    hid=hid
    bookinginfo = Bookinginfo.objects.get(id=id)
    hotelinfo = Hotelinfo.objects.get(id=hid)
    if request.method == 'POST':
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        mode = request.POST.get('mode')
        info = request.POST.get('info')

        Paymentinfo.objects.create(Bookingkey=bookinginfo,Hpaymentskey=hotelinfo,Payment_Type='Hotel',Amount=amount,Date=date,
                                    Mode_of_payment=mode,Additional_info=info)
        amtpaid=Paymentinfo.objects.filter(Hpaymentskey=hotelinfo).aggregate(Sum('Amount'))
        print(amtpaid)
        Hotelinfo.objects.filter(id=hid).update(Amount_Paid=int(amtpaid['Amount__sum']))
        tcost =Hotelinfo.objects.filter(id=hid).values_list('Total_Cost', flat=True)[0]
        Hotelinfo.objects.filter(id=hid).update(due_amount=tcost-amtpaid['Amount__sum'])
    return render(request, 'hotelpayments.html',{'id':id})

def transport_payments(request,id,tid):
    id=id
    tid=tid
    bookinginfo = Bookinginfo.objects.get(id=id)
    transportinfo = Transportinfo.objects.get(id=tid)
    if request.method == 'POST':
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        mode = request.POST.get('mode')
        info = request.POST.get('info')

        Paymentinfo.objects.create(Bookingkey=bookinginfo,Tpaymentskey=transportinfo,Payment_Type='Transport',Amount=amount,Date=date,
                                    Mode_of_payment=mode,Additional_info=info)
        amtpaid=Paymentinfo.objects.filter(Tpaymentskey=transportinfo).aggregate(Sum('Amount'))
        Transportinfo.objects.filter(id=tid).update(Amount_Paid=amtpaid['Amount__sum'])
        tcost =Transportinfo.objects.filter(id=tid).values_list('Total_Cost', flat=True)[0]
        Transportinfo.objects.filter(id=tid).update(Due_Amount=tcost-amtpaid['Amount__sum'])
    return render(request, 'hotelpayments.html',{'id':id})

def activity_payments(request,id,aid):
    id=id
    aid=aid
    bookinginfo = Bookinginfo.objects.get(id=id)
    activityinfo = Activitiesinfo.objects.get(id=aid)
    if request.method == 'POST':
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        mode = request.POST.get('mode')
        info = request.POST.get('info')

        Paymentinfo.objects.create(Bookingkey=bookinginfo,Apaymentskey=activityinfo,Payment_Type='Activity',Amount=amount,Date=date,
                                    Mode_of_payment=mode,Additional_info=info)
        amtpaid=Paymentinfo.objects.filter(Apaymentskey=activityinfo).aggregate(Sum('Amount'))
        Activitiesinfo.objects.filter(id=aid).update(Amount_Paid=amtpaid['Amount__sum'])
        tcost =Activitiesinfo.objects.filter(id=aid).values_list('Total_Cost', flat=True)[0]
        Activitiesinfo.objects.filter(id=aid).update(Due_Amount=tcost-amtpaid['Amount__sum'])
    return render(request, 'hotelpayments.html',{'id':id})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('a')
        else:
           messages.success(request,("User not Registered, access denied!"))
           return redirect('/')

    else:
        return render(request,'login.html')