from django.shortcuts import render , redirect
from django.conf import settings
from django.core.mail import send_mail , EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
import os

def index(request):
    if request.method == 'POST':
        hotel_name = request.POST.get('hotel-name')
        hotel_city = request.POST.get('hotel-city')
        hotel_mail_ids = request.POST.get('mail-id')
        concern_person_name = request.POST.get('concern-person-name')

        hotel_mail_id = hotel_mail_ids.split(',')

        print(hotel_mail_id)

        context = {
            'hotel_name':hotel_name,
            'hotel_city':hotel_city,
            'concern_person_name':concern_person_name
        }
        file_path = os.path.join(settings.BASE_DIR, r'static\pdf\Universal-Adventures.pdf')
        file = open(file_path,'r')

        message_body = render_to_string('mail.html',context)

        mail = EmailMessage(
        subject=f"Regarding Collaboration – {hotel_name} – Universal Adventures",
        body=message_body,
        from_email = 'booking@universaladventure.in',
#        from_email=settings.EMAIL_HOST_USER,
        to=hotel_mail_id)
        mail.content_subtype = "html"
        mail.attach_file(file.name, 'application/pdf')
        mail.send()
        messages.info(request,'mail sended successfully')
    return render(request,'index.html',{})
