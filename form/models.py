from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.aggregates import Count, Sum
from django.utils import timezone
import string
import random



class PersonalInfo(models.Model):
    GENDER = [
            ('Male','Male'),
            ('Female','Female'),
        ]

    Name = models.CharField(max_length=255)
    Email = models.EmailField(null=True)
    PhoneNo = models.CharField(max_length=255)
    DOB = models.DateField(default=datetime.date.today, null=True)
    Gender = models.CharField(max_length=255,choices=GENDER, null=True)
    Occupation = models.CharField(max_length = 255,null=True)
    Address = models.CharField(max_length=255, null=True)
    City = models.CharField(max_length=255,null=True)
    State = models.CharField(max_length = 255,null=True)
    Aadhar_Card_No = models.CharField(max_length=12, null=True)
    
    
    
    
    
    

    def __str__(self):
        return str(self.id)


class Bookinginfo(models.Model):
    personal_details = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, null=True, blank=True,related_name='bdetails')
    Bookingkey = models.CharField(max_length=255, default="")
    Trip_Name = models.CharField(max_length=255, null=True)
    Start_Date = models.DateField(default=datetime.date.today)
    End_Date = models.DateField(default=datetime.date.today)
    City = models.CharField(max_length=255)
    State = models.CharField(max_length=255)
    Service = models.CharField(max_length=255, null=True)
    Total_Cost = models.PositiveIntegerField(null=True)
    Amount_Paid = models.PositiveIntegerField(null=True)
    Due_amount = models.PositiveIntegerField(null=True)
    BookingDate = models.DateField(default=datetime.date.today)
    Mode_of_payment = models.CharField(max_length=255, null=True)
    Additional_info = models.CharField(max_length=255, null=True)
    Created_by = models.CharField(max_length=255, null=True)
    Due_Date = models.DateField(default=datetime.date.today)
    Service_Status = models.CharField(max_length=255, null=True)
    No_of_People = models.CharField(max_length=255, null=True)
    Trello_link = models.CharField(max_length=255,null=True)

    @property
    def due_amt(self):
        due = self.Total_Cost - self.Amount_Paid
        return due

    @property
    def total_hbookings(self):
        hbookings = self.hotelinfo_set.all()
        count = 0
        for booking in hbookings:
                count += 1
        return count

    @property
    def bhbookings(self):
        hbookings = self.hotelinfo_set.all()
        count = 0
        for booking in hbookings:
            if booking.Service_Status=='Booked':
                count += 1
        return count

    @property
    def total_abookings(self):
        abookings = self.activitiesinfo_set.all()
        count = 0
        for booking in abookings:
                count += 1
        return count

    @property
    def babookings(self):
        abookings = self.activitiesinfo_set.all()
        count = 0
        for booking in abookings:
            if booking.Service_Status=='Booked':
                count += 1
        return count

    @property
    def total_tbookings(self):
        tbookings = self.transportinfo_set.all()
        count = 0
        for booking in tbookings:
                count += 1
        return count

    @property
    def btbookings(self):
        tbookings = self.transportinfo_set.all()
        count = 0
        for booking in tbookings:
            if booking.Service_Status=='Booked':
                count += 1
        return count

    @property
    def total_tibookings(self):
        tibookings = self.ticketinfo_set.all()
        count = 0
        for booking in tibookings:
                count += 1
        return count

    @property
    def btibookings(self):
        tibookings = self.ticketinfo_set.all()
        count = 0
        for booking in tibookings:
            if booking.Service_Status=='Booked':
                count += 1
        return count


        

class Hotelinfo(models.Model):
    Bookingkey = models.ForeignKey(Bookinginfo, on_delete=models.CASCADE)
    Hname = models.CharField(max_length=255)
    Hstate = models.CharField(max_length=255,null=True)
    Hcity = models.CharField(max_length=255,null=True)
    Checkin_Date = models.DateField(default=datetime.date.today,null=True)
    Checktout_Date = models.DateField(default=datetime.date.today,null=True)
    No_of_rooms = models.PositiveIntegerField(null=True)
    Room_Type = models.CharField(max_length=255,null=True)
    Meal_Plan = models.CharField(max_length=255,null=True)
    Room_Sharing_Option = models.CharField(max_length=255,null=True)
    Hotel_Contact_Name = models.CharField(max_length=255,null=True)
    Hotel_Contact_No = models.CharField(max_length=255,null=True)
    Hemail = models.EmailField(null=True)
    Total_Cost = models.PositiveIntegerField(null=True)
    Amount_Paid = models.PositiveIntegerField(null=True)
    due_amount = models.PositiveIntegerField(default='0')
    Additional_info = models.CharField(null=True,max_length=255)
    Service_Status = models.CharField(max_length=255, null=True)
   
    @property
    def due_amt(self):
        due = self.Total_Cost - self.Amount_Paid
        return due
    @property
    def totalbookings(self):
        return Count(self.id)


class Activitiesinfo(models.Model):
    Bookingkey = models.ForeignKey(Bookinginfo, on_delete=models.CASCADE)
    Name_of_activity = models.CharField(max_length=255)
    State = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    No_of_People = models.CharField(max_length=255,null=True)
    Date = models.DateField(default=datetime.date.today)
    Vendor_Name = models.CharField(max_length=255)
    Vendor_Contact_No = models.CharField(max_length=255)
    Total_Cost = models.PositiveIntegerField()
    Amount_Paid = models.PositiveBigIntegerField(null=True)
    Due_Amount = models.PositiveIntegerField(default='0')
    Additional_info = models.CharField(max_length=255,null=True)
    Service_Status = models.CharField(max_length=255, null=True)

    @property
    def due_amt(self):
        due = self.Total_Cost - self.Amount_Paid
        return due

class Ticketinfo(models.Model):
    Bookingkey = models.ForeignKey(Bookinginfo, on_delete=models.CASCADE)
    Type_of_ticket = models.CharField(max_length=255)
    No_of_tickets = models.PositiveIntegerField()
    Departure_Date = models.DateField(default=datetime.date.today)
    Arrival_Date = models.DateField(default=datetime.date.today)
    Departure_city = models.CharField(max_length=255)
    Arrival_city = models.CharField(max_length=255)
    Total_Cost = models.PositiveIntegerField()
    Amount_Paid = models.PositiveIntegerField(null=True)
    Due_Amount = models.PositiveIntegerField(null=True)
    Additional_info = models.CharField(max_length=255)
    Service_Status = models.CharField(max_length=255, null=True)
   

class Transportinfo(models.Model):
    Bookingkey = models.ForeignKey(Bookinginfo, on_delete=models.CASCADE)
    Vehicle_Name = models.CharField(max_length=255)
    Driver_Name = models.CharField(max_length=255)
    Driver_Phone_No = models.CharField(max_length=255)
    Start_Date = models.DateField(default=datetime.date.today)
    End_date = models.DateField(default=datetime.date.today)
    Start_Location = models.CharField(max_length=255)
    End_Location = models.CharField(max_length=255)
    Total_Cost = models.PositiveIntegerField()
    Amount_Paid = models.PositiveBigIntegerField(null=True)
    Due_Amount = models.PositiveIntegerField(null=True)
    Additional_info = models.CharField(max_length=255)    
    Service_Status = models.CharField(max_length=255, null=True)

    @property
    def due_amt(self):
        due = self.Total_Cost - self.Amount_Paid
        return due
        
class Paymentinfo(models.Model):
    Bookingkey = models.ForeignKey(Bookinginfo, on_delete=models.CASCADE)
    Hpaymentskey = models.ForeignKey(Hotelinfo,null=True,on_delete=models.CASCADE,related_name='hp')
    Tpaymentskey = models.ForeignKey(Transportinfo,null=True,on_delete=models.CASCADE,related_name='tp')
    Apaymentskey = models.ForeignKey(Activitiesinfo,null=True,on_delete=models.CASCADE,related_name='ap')
    Tipaymentskey = models.ForeignKey(Ticketinfo,null=True,on_delete=models.CASCADE,related_name='tip')
    Payment_Type = models.CharField(max_length=255)
    Amount = models.PositiveBigIntegerField()
    Date = models.DateField(default=datetime.date.today)
    Mode_of_payment = models.CharField(max_length=255)
    Additional_info = models.CharField(max_length=255)
    Verify = models.CharField(max_length=255)


class Connections(models.Model):
    Bookingkey = models.ForeignKey(Bookinginfo, on_delete=models.CASCADE)
    Personalkey = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE,related_name='connections')
    Membertype = models.CharField(max_length=255)

class Commentinfo(models.Model):
     Bookingkey = models.ForeignKey(Bookinginfo, on_delete=models.CASCADE,related_name='bp')
     Hopaymentskey = models.ForeignKey(Hotelinfo,null=True,on_delete=models.CASCADE,related_name='hop')
     Trpaymentskey = models.ForeignKey(Transportinfo,null=True,on_delete=models.CASCADE,related_name='trp')
     Acpaymentskey = models.ForeignKey(Activitiesinfo,null=True,on_delete=models.CASCADE,related_name='acp')
     Ticpaymentskey = models.ForeignKey(Ticketinfo,null=True,on_delete=models.CASCADE,related_name='ticp')
     Comment_Type = models.CharField(max_length=255)
     duedate = models.DateField(default=datetime.date.today)
     Comment = models.TextField()
     User = models.CharField(max_length=255)
     Time = models.DateTimeField(default=timezone.now)
     Tag = models.CharField(max_length=255)

class Usercreatedby(models.Model):
    user = models.CharField(max_length=255)
    created_by = models.CharField(max_length=255)



class Venderinfo(models.Model):

    STATES = [
        ("Andhra Pradesh",	"Andhra Pradesh"),
("AR",	"Arunachal Pradesh"),
("AS",	"Assam"),
("BR",	"Bihar"),
("CT",	"Chhattisgarh"),
("GA",	"Goa"),
("GJ",	"Gujarat"),
("HR",	"Haryana"),
("HP",	"Himachal Pradesh"),
("JK",	"Jammu and Kashmir"),
("JH",	"Jharkhand"),
("KA",	"Karnataka"),
("KL",	"Kerala"),
("MP",	"Madhya Pradesh"),
("Maharashtra",	"Maharashtra"),
("MN",	"Manipur"),
("ML",	"Meghalaya"),
("MZ",	"Mizoram"),
("NL",	"Nagaland"),
("OR",	"Odisha"),
("PB",	"Punjab"),
("RJ",	"Rajasthan"),
("SK",	"Sikkim"),
("TN",	"Tamil Nadu"),
("TG",	"Telangana"),
("TR",	"Tripura"),
("UP",	"Uttar Pradesh"),
("UT",	"Uttarakhand"),
("WB",	"West Bengal"),
("AN",	"Andaman and Nicobar Islands"),
("CH",	"Chandigarh"),
("DN",	"Dadra and Nagar Haveli"),
("DD",	"Daman and Diu"),
("LD",	"Lakshadweep"),
("DL",	"Delhi"),
("PY",	"Puducherry")
    ]
    
    cities = (
        ("Andaman and Nicobar Islands", (("Port Blair", "Port Blair"),)),
     (
        "Andhra Pradesh",
        (
            ("Visakhapatnam", "Visakhapatnam"),
            ("Vijayawada", "Vijayawada"),
            ("Guntur", "Guntur"),
            ("Nellore", "Nellore"),
            ("Kurnool", "Kurnool"),
            ("Rajamahendravaram", "Rajamahendravaram"),
            ("Tirupati", "Tirupati"),
            ("Kadapa", "Kadapa"),
            ("Kakinada", "Kakinada"),
            ("Anantapur", "Anantapur"),
            ("Vizianagaram", "Vizianagaram"),
            ("Eluru", "Eluru"),
            ("Ongole", "Ongole"),
            ("Nandyal", "Nandyal"),
            ("Machilipatnam", "Machilipatnam"),
            ("Adoni", "Adoni"),
            ("Tenali", "Tenali"),
            ("Proddatur", "Proddatur"),
            ("Chittoor", "Chittoor"),
            ("Hindupur", "Hindupur"),
            ("Bhimavaram", "Bhimavaram"),
            ("Madanapalle", "Madanapalle"),
            ("Guntakal", "Guntakal"),
            ("Srikakulam", "Srikakulam"),
            ("Dharmavaram", "Dharmavaram"),
            ("Gudivada", "Gudivada"),
            ("Narasaraopet", "Narasaraopet"),
            ("Tadipatri", "Tadipatri"),
            ("Tadepalligudem", "Tadepalligudem"),
            ("Amaravati", "Amaravati"),
            ("Chilakaluripet", "Chilakaluripet"),
        ),
    ),
    (
        "Bihar",
        (
            ("Patna", "Patna"),
            ("Gaya", "Gaya"),
            ("Bhagalpur", "Bhagalpur"),
            ("Muzaffarpur", "Muzaffarpur"),
            ("Purnia", "Purnia"),
            ("Darbhanga", "Darbhanga"),
            ("Bihar Sharif", "Bihar Sharif"),
            ("Arrah", "Arrah"),
            ("Begusarai", "Begusarai"),
            ("Katihar", "Katihar"),
            ("Munger", "Munger"),
            ("Chhapra", "Chhapra"),
            ("Bettiah", "Bettiah"),
            ("Saharsa", "Saharsa"),
            ("Hajipur", "Hajipur"),
            ("Sasaram", "Sasaram"),
            ("Dehri", "Dehri"),
            ("Siwan", "Siwan"),
            ("Motihari", "Motihari"),
            ("Nawada", "Nawada"),
            ("Bagaha", "Bagaha"),
            ("Buxar", "Buxar"),
            ("Kishanganj", "Kishanganj"),
            ("Sitamarhi", "Sitamarhi"),
            ("Jamalpur", "Jamalpur"),
            ("Jehanabad", "Jehanabad"),
            ("Aurangabad", "Aurangabad"),
            ("Lakhisarai", "Lakhisarai"),
        ),
    ),
    ("Chandigarh", (("Chandigarh", "Chandigarh"),),),
    (
        "Chhattisgarh",
        (
            ("Raipur", "Raipur"),
            ("Durg", "Durg"),
            ("Naya Raipur", "Naya Raipur"),
            ("Korba", "Korba"),
            ("Bilaspur", "Bilaspur"),
            ("Rajnandgaon", "Rajnandgaon"),
            ("Pakhanjore", "Pakhanjore"),
            ("Jagdalpur", "Jagdalpur"),
            ("Ambikapur", "Ambikapur"),
            ("Chirmiri", "Chirmiri"),
            ("Dhamtari", "Dhamtari"),
            ("Raigarh", "Raigarh"),
            ("Mahasamund", "Mahasamund"),
        ),
    ),
    ("Daman and Diu", (("Daman", "Daman"),),),
    ("Delhi", (("Delhi", "Delhi"),),),
    ("Dadra and Nagar Haveli", (("Silvassa", "Silvassa"),),),
    (
        "Goa",
        (
            ("Panaji", "Panaji"),
            ("Vasco", "Vasco"),
            ("Mormugao", "Mormugao"),
            ("Margao", "Margao"),
        ),
    ),
    (
        "Gujarat",
        (
            ("Ahmedabad", "Ahmedabad"),
            ("Surat", "Surat"),
            ("Vadodara", "Vadodara"),
            ("Rajkot", "Rajkot"),
            ("Bhavnagar", "Bhavnagar"),
            ("Jamnagar", "Jamnagar"),
            ("Junagadh", "Junagadh"),
            ("Gandhidham", "Gandhidham"),
            ("Nadiad", "Nadiad"),
            ("Gandhinagar", "Gandhinagar"),
            ("Anand", "Anand"),
            ("Morbi", "Morbi"),
            ("Khambhat", "Khambhat"),
            ("Surendranagar", "Surendranagar"),
            ("Bharuch", "Bharuch"),
            ("Vapi", "Vapi"),
            ("Navsari", "Navsari"),
            ("Veraval", "Veraval"),
            ("Porbandar", "Porbandar"),
            ("Godhra", "Godhra"),
            ("Bhuj", "Bhuj"),
            ("Ankleshwar", "Ankleshwar"),
            ("Botad", "Botad"),
            ("Patan", "Patan"),
            ("Palanpur", "Palanpur"),
            ("Dahod", "Dahod"),
            ("Jetpur", "Jetpur"),
            ("Valsad", "Valsad"),
            ("Kalol", "Kalol"),
            ("Gondal", "Gondal"),
            ("Deesa", "Deesa"),
            ("Amreli", "Amreli"),
            ("Amreli", "Amreli"),
            ("Mahuva", "Mahuva"),
            ("Mehsana", "Mehsana"),
        ),
    ),
    ("Himachal Pradesh", (("Shimla", "Shimla"),),),
    (
        "Haryana",
        (
            ("Faridabad", "Faridabad"),
            ("Gurgaon", "Gurgaon"),
            ("Panipat", "Panipat"),
            ("Ambala", "Ambala"),
            ("Yamunanagar", "Yamunanagar"),
            ("Rohtak", "Rohtak"),
            ("Hisar", "Hisar"),
            ("Karnal", "Karnal"),
            ("Sonipat", "Sonipat"),
            ("Panchkula", "Panchkula"),
            ("Bhiwani", "Bhiwani"),
            ("Sirsa", "Sirsa"),
            ("Bahadurgarh", "Bahadurgarh"),
            ("Jind", "Jind"),
            ("Thanesar", "Thanesar"),
            ("Kaithal", "Kaithal"),
            ("Rewari", "Rewari"),
            ("Palwal", "Palwal"),
        ),
    ),
    (
        "Jharkhand",
        (
            ("Jamshedpur", "Jamshedpur"),
            ("Dhanbad", "Dhanbad"),
            ("Ranchi", "Ranchi"),
            ("Bokaro Steel City", "Bokaro Steel City"),
            ("Deoghar", "Deoghar"),
            ("Phusro", "Phusro"),
            ("Hazaribagh", "Hazaribagh"),
            ("Giridih", "Giridih"),
            ("Ramgarh", "Ramgarh"),
            ("Medininagar", "Medininagar"),
            ("Chirkunda", "Chirkunda"),
            ("Jhumri Telaiya", "Jhumri Telaiya"),
            ("Sahibganj", "Sahibganj"),
        ),
    ),
    (
        "Jammu and Kashmir",
        (("Srinagar", "Srinagar"), ("Jammu", "Jammu"), ("Anantnag", "Anantnag"),),
    ),
    (
        "Karnataka",
        (
            ("Bengaluru", "Bengaluru"),
            ("Hubli", "Hubli"),
            ("Mysore", "Mysore"),
            ("Gulbarga", "Gulbarga"),
            ("Mangalore", "Mangalore"),
            ("Belgaum", "Belgaum"),
            ("Davangere", "Davangere"),
            ("Bellary", "Bellary"),
            ("Bijapur", "Bijapur"),
            ("Shimoga", "Shimoga"),
            ("Tumkur", "Tumkur"),
            ("Raichur", "Raichur"),
            ("Bidar", "Bidar"),
            ("Hospet", "Hospet"),
            ("Hassan", "Hassan"),
            ("Gadag", "Gadag"),
            ("Udupi", "Udupi"),
            ("Robertsonpet", "Robertsonpet"),
            ("Bhadravati", "Bhadravati"),
            ("Chitradurga", "Chitradurga"),
            ("Harihar", "Harihar"),
            ("Kolar", "Kolar"),
            ("Mandya", "Mandya"),
            ("Chikkamagallooru", "Chikkamagallooru"),
            ("Chikmagalur", "Chikmagalur"),
            ("Gangawati", "Gangawati"),
            ("Ranebennuru", "Ranebennuru"),
            ("Ramanagara", "Ramanagara"),
            ("Bagalkot", "Bagalkot"),
        ),
    ),
    (
        "Kerala",
        (
            ("Thiruvananthapuram", "Thiruvananthapuram"),
            ("Kochi", "Kochi"),
            ("Calicut", "Calicut"),
            ("Kollam", "Kollam"),
            ("Thrissur", "Thrissur"),
            ("Kannur", "Kannur"),
            ("Kasaragod", "Kasaragod"),
            ("Alappuzha", "Alappuzha"),
            ("Alappuzha", "Alappuzha"),
            ("Palakkad", "Palakkad"),
            ("Kottayam", "Kottayam"),
            ("Kothamangalam", "Kothamangalam"),
            ("Malappuram", "Malappuram"),
            ("Manjeri", "Manjeri"),
            ("Thalassery", "Thalassery"),
            ("Ponnani", "Ponnani"),
        ),
    ),
    ("Lakshadweep", (("Kavaratti", "Kavaratti"),),),
    (
        "Maharashtra",
        (
            ("Mumbai", "Mumbai"),
            ("Pune", "Pune"),
            ("Nagpur", "Nagpur"),
            ("Nashik", "Nashik"),
            ("Pimpri-Chinchwad", "Pimpri-Chinchwad"),
            ("Aurangabad", "Aurangabad"),
            ("Solapur", "Solapur"),
            ("Bhiwandi", "Bhiwandi"),
            ("Amravati", "Amravati"),
            ("Nanded", "Nanded"),
            ("Kolhapur", "Kolhapur"),
            ("Sangli-Miraj-Kupwad", "Sangli-Miraj-Kupwad"),
            ("Jalgaon", "Jalgaon"),
            ("Akola", "Akola"),
            ("Latur", "Latur"),
            ("Malegaon", "Malegaon"),
            ("Dhule", "Dhule"),
            ("Ahmednagar", "Ahmednagar"),
            ("Nandurbar", "Nandurbar"),
            ("Ichalkaranji", "Ichalkaranji"),
            ("Chandrapur", "Chandrapur"),
            ("Jalna", "Jalna"),
            ("Parbhani", "Parbhani"),
            ("Bhusawal", "Bhusawal"),
            ("Satara", "Satara"),
            ("Beed", "Beed"),
            ("Pandharpur", "Pandharpur"),
            ("Yavatmal", "Yavatmal"),
            ("Kamptee", "Kamptee"),
            ("Gondia", "Gondia"),
            ("Achalpur", "Achalpur"),
            ("Osmanabad", "Osmanabad"),
            ("Hinganghat", "Hinganghat"),
            ("Wardha", "Wardha"),
            ("Barshi", "Barshi"),
            ("Chalisgaon", "Chalisgaon"),
            ("Amalner", "Amalner"),
            ("Khamgaon", "Khamgaon"),
            ("Akot", "Akot"),
            ("Udgir", "Udgir"),
            ("Bhandara", "Bhandara"),
            ("Parli", "Parli"),
        ),
    ),
    ("Meghalaya", (("Shillong", "Shillong"),),),
    ("Manipur", (("Imphal", "Imphal"),),),
    (
        "Madhya Pradesh",
        (
            ("Indore", "Indore"),
            ("Bhopal", "Bhopal"),
            ("Jabalpur", "Jabalpur"),
            ("Gwalior", "Gwalior"),
            ("Ujjain", "Ujjain"),
            ("Sagar", "Sagar"),
            ("Dewas", "Dewas"),
            ("Satna", "Satna"),
            ("Ratlam", "Ratlam"),
            ("Rewa", "Rewa"),
            ("Katni", "Katni"),
            ("Singrauli", "Singrauli"),
            ("Burhanpur", "Burhanpur"),
            ("Khandwa", "Khandwa"),
            ("Morena", "Morena"),
            ("Bhind", "Bhind"),
            ("Chhindwara", "Chhindwara"),
            ("Guna", "Guna"),
            ("Shivpuri", "Shivpuri"),
            ("Vidisha", "Vidisha"),
            ("Chhatarpur", "Chhatarpur"),
            ("Damoh", "Damoh"),
            ("Mandsaur", "Mandsaur"),
            ("Khargone", "Khargone"),
            ("Neemuch", "Neemuch"),
            ("Pithampur", "Pithampur"),
            ("Hoshangabad", "Hoshangabad"),
            ("Itarsi", "Itarsi"),
            ("Sehore", "Sehore"),
            ("Betul", "Betul"),
            ("Seoni", "Seoni"),
            ("Datia", "Datia"),
            ("Nagda", "Nagda"),
            ("Dhanpuri", "Dhanpuri"),
            ("Dhar", "Dhar"),
            ("Balaghat", "Balaghat"),
        ),
    ),
    ("Mizoram", (("Aizawl", "Aizawl"),),),
    ("Nagaland", (("Dimapur", "Dimapur"), ("Kohima", "Kohima"),),),
    (
        "Odisha",
        (
            ("Bhubaneswar", "Bhubaneswar"),
            ("Cuttack", "Cuttack"),
            ("Rourkela", "Rourkela"),
            ("Berhampur", "Berhampur"),
            ("Sambalpur", "Sambalpur"),
            ("Puri", "Puri"),
            ("Balasore", "Balasore"),
            ("Bhadrak", "Bhadrak"),
            ("Baripada", "Baripada"),
            ("Balangir", "Balangir"),
            ("Jharsuguda", "Jharsuguda"),
            ("Jeypore", "Jeypore"),
        ),
    ),
    (
        "Punjab",
        (
            ("Ludhiana", "Ludhiana"),
            ("Amritsar", "Amritsar"),
            ("Jalandhar", "Jalandhar"),
            ("Patiala", "Patiala"),
            ("Bathinda", "Bathinda"),
            ("Hoshiarpur", "Hoshiarpur"),
            ("Batala", "Batala"),
            ("Mohali", "Mohali"),
            ("Abohar", "Abohar"),
            ("Pathankot", "Pathankot"),
            ("Moga", "Moga"),
            ("Malerkotla", "Malerkotla"),
            ("Khanna", "Khanna"),
            ("Muktasar", "Muktasar"),
            ("Barnala", "Barnala"),
            ("Firozpur", "Firozpur"),
            ("Kapurthala", "Kapurthala"),
            ("Phagwara", "Phagwara"),
            ("Zirakpur", "Zirakpur"),
            ("Rajpura", "Rajpura"),
        ),
    ),
    (
        "Puducherry",
        (
            ("Pondicherry", "Pondicherry"),
            ("Ozhukarai", "Ozhukarai"),
            ("Karaikal", "Karaikal"),
        ),
    ),
    (
        "Rajasthan",
        (
            ("Jaipur", "Jaipur"),
            ("Jodhpur", "Jodhpur"),
            ("Kota", "Kota"),
            ("Bikaner", "Bikaner"),
            ("Ajmer", "Ajmer"),
            ("Udaipur", "Udaipur"),
            ("Bhilwara", "Bhilwara"),
            ("Alwar", "Alwar"),
            ("Bharatpur", "Bharatpur"),
            ("Sri Ganganagar", "Sri Ganganagar"),
            ("Sikar", "Sikar"),
            ("Pali", "Pali"),
            ("Barmer", "Barmer"),
            ("Tonk", "Tonk"),
            ("Kishangarh", "Kishangarh"),
            ("Chittorgarh", "Chittorgarh"),
            ("Beawar", "Beawar"),
            ("Hanumangarh", "Hanumangarh"),
            ("Dholpur", "Dholpur"),
            ("Gangapur", "Gangapur"),
            ("Sawai Madhopur", "Sawai Madhopur"),
            ("Churu", "Churu"),
            ("Baran", "Baran"),
            ("Makrana", "Makrana"),
            ("Nagaur", "Nagaur"),
            ("Hindaun", "Hindaun"),
            ("Bhiwadi", "Bhiwadi"),
            ("Bundi", "Bundi"),
            ("Sujangarh", "Sujangarh"),
            ("Jhunjhunu", "Jhunjhunu"),
            ("Banswara", "Banswara"),
            ("Sardarshahar", "Sardarshahar"),
            ("Fatehpur", "Fatehpur"),
            ("Dausa", "Dausa"),
            ("Karauli", "Karauli"),
        ),
    ),
    ("Sikkim", (("Gangtok", "Gangtok"),),),
    (
        "Telangana",
        (
            ("Hyderabad", "Hyderabad"),
            ("Warangal", "Warangal"),
            ("Nizamabad", "Nizamabad"),
            ("Karimnagar", "Karimnagar"),
            ("Ramagundam", "Ramagundam"),
            ("Khammam", "Khammam"),
            ("Mahbubnagar", "Mahbubnagar"),
            ("Nalgonda", "Nalgonda"),
            ("Adilabad", "Adilabad"),
            ("Siddipet", "Siddipet"),
            ("Suryapet", "Suryapet"),
            ("Miryalaguda", "Miryalaguda"),
            ("Jagtial", "Jagtial"),
            ("Mancherial", "Mancherial"),
            ("Kothagudem", "Kothagudem"),
        ),
    ),
    (
        "Tamil Nadu",
        (
            ("Chennai", "Chennai"),
            ("Coimbatore", "Coimbatore"),
            ("Madurai", "Madurai"),
            ("Tiruchirappalli", "Tiruchirappalli"),
            ("Tirupur", "Tirupur"),
            ("Salem", "Salem"),
            ("Erode", "Erode"),
            ("Tirunelveli", "Tirunelveli"),
            ("Vellore", "Vellore"),
            ("Tuticorin", "Tuticorin"),
            ("Gudiyatham", "Gudiyatham"),
            ("Nagercoil", "Nagercoil"),
            ("Thanjavur", "Thanjavur"),
            ("Dindigul", "Dindigul"),
            ("Vaniyambadi", "Vaniyambadi"),
            ("Cuddalore", "Cuddalore"),
            ("Komarapalayam", "Komarapalayam"),
            ("Kanchipuram", "Kanchipuram"),
            ("Ambur", "Ambur"),
            ("Tiruvannamalai", "Tiruvannamalai"),
            ("Pudukkottai", "Pudukkottai"),
            ("Kumbakonam", "Kumbakonam"),
            ("Rajapalayam", "Rajapalayam"),
            ("Hosur", "Hosur"),
            ("Karaikudi", "Karaikudi"),
            ("Neyveli", "Neyveli"),
            ("Nagapattinam", "Nagapattinam"),
            ("Viluppuram", "Viluppuram"),
            ("Paramakudi", "Paramakudi"),
            ("Tiruchengode", "Tiruchengode"),
            ("Kovilpatti", "Kovilpatti"),
            ("Theni-Allinagaram", "Theni-Allinagaram"),
            ("Kadayanallur", "Kadayanallur"),
            ("Pollachi", "Pollachi"),
            ("Ooty", "Ooty"),
        ),
    ),
    ("Tripura", (("Agartala", "Agartala"),),),
    (
        "Uttar Pradesh",
        (
            ("Kanpur", "Kanpur"),
            ("Lucknow", "Lucknow"),
            ("Ghaziabad", "Ghaziabad"),
            ("Agra", "Agra"),
            ("Varanasi", "Varanasi"),
            ("Meerut", "Meerut"),
            ("Allahabad", "Allahabad"),
            ("Bareilly", "Bareilly"),
            ("Aligarh", "Aligarh"),
            ("Moradabad", "Moradabad"),
            ("Saharanpur", "Saharanpur"),
            ("Gorakhpur", "Gorakhpur"),
            ("Faizabad", "Faizabad"),
            ("Firozabad", "Firozabad"),
            ("Jhansi", "Jhansi"),
            ("Muzaffarnagar", "Muzaffarnagar"),
            ("Mathura", "Mathura"),
            ("Budaun", "Budaun"),
            ("Rampur", "Rampur"),
            ("Shahjahanpur", "Shahjahanpur"),
            ("Farrukhabad", "Farrukhabad"),
            ("Mau", "Mau"),
            ("Hapur", "Hapur"),
            ("Noida", "Noida"),
            ("Etawah", "Etawah"),
            ("Mirzapur", "Mirzapur"),
            ("Bulandshahr", "Bulandshahr"),
            ("Sambhal", "Sambhal"),
            ("Amroha", "Amroha"),
            ("Hardoi", "Hardoi"),
            ("Fatehpur", "Fatehpur"),
            ("Raebareli", "Raebareli"),
            ("Orai", "Orai"),
            ("Sitapur", "Sitapur"),
            ("Bahraich", "Bahraich"),
            ("Modinagar", "Modinagar"),
            ("Unnao", "Unnao"),
            ("Jaunpur", "Jaunpur"),
            ("Lakhimpur", "Lakhimpur"),
            ("Hathras", "Hathras"),
            ("Banda", "Banda"),
            ("Pilibhit", "Pilibhit"),
            ("Barabanki", "Barabanki"),
            ("Mughalsarai", "Mughalsarai"),
            ("Khurja", "Khurja"),
            ("Gonda", "Gonda"),
            ("Mainpuri", "Mainpuri"),
            ("Lalitpur", "Lalitpur"),
            ("Etah", "Etah"),
            ("Deoria", "Deoria"),
            ("Ujhani", "Ujhani"),
            ("Ghazipur", "Ghazipur"),
            ("Sultanpur", "Sultanpur"),
            ("Azamgarh", "Azamgarh"),
            ("Bijnor", "Bijnor"),
            ("Sahaswan", "Sahaswan"),
            ("Basti", "Basti"),
            ("Chandausi", "Chandausi"),
            ("Akbarpur", "Akbarpur"),
            ("Ballia", "Ballia"),
            ("Mubarakpur", "Mubarakpur"),
            ("Tanda", "Tanda"),
            ("Greater Noida", "Greater Noida"),
            ("Shikohabad", "Shikohabad"),
            ("Shamli", "Shamli"),
            ("Baraut", "Baraut"),
            ("Khair", "Khair"),
            ("Kasganj", "Kasganj"),
            ("Auraiya", "Auraiya"),
            ("Khatauli", "Khatauli"),
            ("Deoband", "Deoband"),
            ("Nagina", "Nagina"),
            ("Mahoba", "Mahoba"),
            ("Muradnagar", "Muradnagar"),
            ("Bhadohi", "Bhadohi"),
            ("Dadri", "Dadri"),
            ("Pratapgarh", "Pratapgarh"),
            ("Najibabad", "Najibabad"),
        ),
    ),
    (
        "Uttarakhand",
        (
            ("Dehradun", "Dehradun"),
            ("Haridwar", "Haridwar"),
            ("Roorkee", "Roorkee"),
            ("Haldwani", "Haldwani"),
            ("Rudrapur", "Rudrapur"),
            ("Kashipur", "Kashipur"),
            ("Rishikesh", "Rishikesh"),
        ),
    ),
    (
        "West Bengal",
        (
            ("Kolkata", "Kolkata"),
            ("Asansol", "Asansol"),
            ("Siliguri", "Siliguri"),
            ("Durgapur", "Durgapur"),
            ("Bardhaman", "Bardhaman"),
            ("Malda", "Malda"),
            ("Baharampur", "Baharampur"),
            ("Habra", "Habra"),
            ("Jalpaiguri", "Jalpaiguri"),
            ("Kharagpur", "Kharagpur"),
            ("Shantipur", "Shantipur"),
            ("Dankuni", "Dankuni"),
            ("Dhulian", "Dhulian"),
            ("Ranaghat", "Ranaghat"),
            ("Haldia", "Haldia"),
            ("Raiganj", "Raiganj"),
            ("Krishnanagar", "Krishnanagar"),
            ("Nabadwip", "Nabadwip"),
            ("Midnapore", "Midnapore"),
            ("Balurghat", "Balurghat"),
            ("Basirhat", "Basirhat"),
            ("Bankura", "Bankura"),
            ("Chakdaha", "Chakdaha"),
            ("Darjeeling", "Darjeeling"),
            ("Alipurduar", "Alipurduar"),
            ("Purulia", "Purulia"),
            ("Jangipur", "Jangipur"),
            ("Bangaon", "Bangaon"),
            ("Cooch Behar", "Cooch Behar"),
            ("Bolpur", "Bolpur"),
            ("Kanthi", "Kanthi"),
        ),
    ),
)

    for_user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phoneno = models.CharField(max_length=255)
    state = models.CharField(max_length=255,choices=STATES)
    city =models.CharField(max_length=255,choices=cities)
    


class EntryForm(models.Model):
    TYPE_CHOICES = [
            ('2 Star','2 Star'),
            ('3 Star','3 Star'),
            ('4 Star','4 Star'),
            ('5 Star','5 Star'),
        ]

    STATES = [
        ("Andhra Pradesh",	"Andhra Pradesh"),
("AR",	"Arunachal Pradesh"),
("AS",	"Assam"),
("BR",	"Bihar"),
("CT",	"Chhattisgarh"),
("GA",	"Goa"),
("GJ",	"Gujarat"),
("HR",	"Haryana"),
("HP",	"Himachal Pradesh"),
("JK",	"Jammu and Kashmir"),
("JH",	"Jharkhand"),
("KA",	"Karnataka"),
("KL",	"Kerala"),
("MP",	"Madhya Pradesh"),
("Maharashtra",	"Maharashtra"),
("MN",	"Manipur"),
("ML",	"Meghalaya"),
("MZ",	"Mizoram"),
("NL",	"Nagaland"),
("OR",	"Odisha"),
("PB",	"Punjab"),
("RJ",	"Rajasthan"),
("SK",	"Sikkim"),
("TN",	"Tamil Nadu"),
("TG",	"Telangana"),
("TR",	"Tripura"),
("UP",	"Uttar Pradesh"),
("UT",	"Uttarakhand"),
("WB",	"West Bengal"),
("AN",	"Andaman and Nicobar Islands"),
("CH",	"Chandigarh"),
("DN",	"Dadra and Nagar Haveli"),
("DD",	"Daman and Diu"),
("LD",	"Lakshadweep"),
("DL",	"Delhi"),
("PY",	"Puducherry")
    ]
    
    cities = (
        ("Andaman and Nicobar Islands", (("Port Blair", "Port Blair"),)),
     (
        "Andhra Pradesh",
        (
            ("Visakhapatnam", "Visakhapatnam"),
            ("Vijayawada", "Vijayawada"),
            ("Guntur", "Guntur"),
            ("Nellore", "Nellore"),
            ("Kurnool", "Kurnool"),
            ("Rajamahendravaram", "Rajamahendravaram"),
            ("Tirupati", "Tirupati"),
            ("Kadapa", "Kadapa"),
            ("Kakinada", "Kakinada"),
            ("Anantapur", "Anantapur"),
            ("Vizianagaram", "Vizianagaram"),
            ("Eluru", "Eluru"),
            ("Ongole", "Ongole"),
            ("Nandyal", "Nandyal"),
            ("Machilipatnam", "Machilipatnam"),
            ("Adoni", "Adoni"),
            ("Tenali", "Tenali"),
            ("Proddatur", "Proddatur"),
            ("Chittoor", "Chittoor"),
            ("Hindupur", "Hindupur"),
            ("Bhimavaram", "Bhimavaram"),
            ("Madanapalle", "Madanapalle"),
            ("Guntakal", "Guntakal"),
            ("Srikakulam", "Srikakulam"),
            ("Dharmavaram", "Dharmavaram"),
            ("Gudivada", "Gudivada"),
            ("Narasaraopet", "Narasaraopet"),
            ("Tadipatri", "Tadipatri"),
            ("Tadepalligudem", "Tadepalligudem"),
            ("Amaravati", "Amaravati"),
            ("Chilakaluripet", "Chilakaluripet"),
        ),
    ),
    (
        "Bihar",
        (
            ("Patna", "Patna"),
            ("Gaya", "Gaya"),
            ("Bhagalpur", "Bhagalpur"),
            ("Muzaffarpur", "Muzaffarpur"),
            ("Purnia", "Purnia"),
            ("Darbhanga", "Darbhanga"),
            ("Bihar Sharif", "Bihar Sharif"),
            ("Arrah", "Arrah"),
            ("Begusarai", "Begusarai"),
            ("Katihar", "Katihar"),
            ("Munger", "Munger"),
            ("Chhapra", "Chhapra"),
            ("Bettiah", "Bettiah"),
            ("Saharsa", "Saharsa"),
            ("Hajipur", "Hajipur"),
            ("Sasaram", "Sasaram"),
            ("Dehri", "Dehri"),
            ("Siwan", "Siwan"),
            ("Motihari", "Motihari"),
            ("Nawada", "Nawada"),
            ("Bagaha", "Bagaha"),
            ("Buxar", "Buxar"),
            ("Kishanganj", "Kishanganj"),
            ("Sitamarhi", "Sitamarhi"),
            ("Jamalpur", "Jamalpur"),
            ("Jehanabad", "Jehanabad"),
            ("Aurangabad", "Aurangabad"),
            ("Lakhisarai", "Lakhisarai"),
        ),
    ),
    ("Chandigarh", (("Chandigarh", "Chandigarh"),),),
    (
        "Chhattisgarh",
        (
            ("Raipur", "Raipur"),
            ("Durg", "Durg"),
            ("Naya Raipur", "Naya Raipur"),
            ("Korba", "Korba"),
            ("Bilaspur", "Bilaspur"),
            ("Rajnandgaon", "Rajnandgaon"),
            ("Pakhanjore", "Pakhanjore"),
            ("Jagdalpur", "Jagdalpur"),
            ("Ambikapur", "Ambikapur"),
            ("Chirmiri", "Chirmiri"),
            ("Dhamtari", "Dhamtari"),
            ("Raigarh", "Raigarh"),
            ("Mahasamund", "Mahasamund"),
        ),
    ),
    ("Daman and Diu", (("Daman", "Daman"),),),
    ("Delhi", (("Delhi", "Delhi"),),),
    ("Dadra and Nagar Haveli", (("Silvassa", "Silvassa"),),),
    (
        "Goa",
        (
            ("Panaji", "Panaji"),
            ("Vasco", "Vasco"),
            ("Mormugao", "Mormugao"),
            ("Margao", "Margao"),
        ),
    ),
    (
        "Gujarat",
        (
            ("Ahmedabad", "Ahmedabad"),
            ("Surat", "Surat"),
            ("Vadodara", "Vadodara"),
            ("Rajkot", "Rajkot"),
            ("Bhavnagar", "Bhavnagar"),
            ("Jamnagar", "Jamnagar"),
            ("Junagadh", "Junagadh"),
            ("Gandhidham", "Gandhidham"),
            ("Nadiad", "Nadiad"),
            ("Gandhinagar", "Gandhinagar"),
            ("Anand", "Anand"),
            ("Morbi", "Morbi"),
            ("Khambhat", "Khambhat"),
            ("Surendranagar", "Surendranagar"),
            ("Bharuch", "Bharuch"),
            ("Vapi", "Vapi"),
            ("Navsari", "Navsari"),
            ("Veraval", "Veraval"),
            ("Porbandar", "Porbandar"),
            ("Godhra", "Godhra"),
            ("Bhuj", "Bhuj"),
            ("Ankleshwar", "Ankleshwar"),
            ("Botad", "Botad"),
            ("Patan", "Patan"),
            ("Palanpur", "Palanpur"),
            ("Dahod", "Dahod"),
            ("Jetpur", "Jetpur"),
            ("Valsad", "Valsad"),
            ("Kalol", "Kalol"),
            ("Gondal", "Gondal"),
            ("Deesa", "Deesa"),
            ("Amreli", "Amreli"),
            ("Amreli", "Amreli"),
            ("Mahuva", "Mahuva"),
            ("Mehsana", "Mehsana"),
        ),
    ),
    ("Himachal Pradesh", (("Shimla", "Shimla"),),),
    (
        "Haryana",
        (
            ("Faridabad", "Faridabad"),
            ("Gurgaon", "Gurgaon"),
            ("Panipat", "Panipat"),
            ("Ambala", "Ambala"),
            ("Yamunanagar", "Yamunanagar"),
            ("Rohtak", "Rohtak"),
            ("Hisar", "Hisar"),
            ("Karnal", "Karnal"),
            ("Sonipat", "Sonipat"),
            ("Panchkula", "Panchkula"),
            ("Bhiwani", "Bhiwani"),
            ("Sirsa", "Sirsa"),
            ("Bahadurgarh", "Bahadurgarh"),
            ("Jind", "Jind"),
            ("Thanesar", "Thanesar"),
            ("Kaithal", "Kaithal"),
            ("Rewari", "Rewari"),
            ("Palwal", "Palwal"),
        ),
    ),
    (
        "Jharkhand",
        (
            ("Jamshedpur", "Jamshedpur"),
            ("Dhanbad", "Dhanbad"),
            ("Ranchi", "Ranchi"),
            ("Bokaro Steel City", "Bokaro Steel City"),
            ("Deoghar", "Deoghar"),
            ("Phusro", "Phusro"),
            ("Hazaribagh", "Hazaribagh"),
            ("Giridih", "Giridih"),
            ("Ramgarh", "Ramgarh"),
            ("Medininagar", "Medininagar"),
            ("Chirkunda", "Chirkunda"),
            ("Jhumri Telaiya", "Jhumri Telaiya"),
            ("Sahibganj", "Sahibganj"),
        ),
    ),
    (
        "Jammu and Kashmir",
        (("Srinagar", "Srinagar"), ("Jammu", "Jammu"), ("Anantnag", "Anantnag"),),
    ),
    (
        "Karnataka",
        (
            ("Bengaluru", "Bengaluru"),
            ("Hubli", "Hubli"),
            ("Mysore", "Mysore"),
            ("Gulbarga", "Gulbarga"),
            ("Mangalore", "Mangalore"),
            ("Belgaum", "Belgaum"),
            ("Davangere", "Davangere"),
            ("Bellary", "Bellary"),
            ("Bijapur", "Bijapur"),
            ("Shimoga", "Shimoga"),
            ("Tumkur", "Tumkur"),
            ("Raichur", "Raichur"),
            ("Bidar", "Bidar"),
            ("Hospet", "Hospet"),
            ("Hassan", "Hassan"),
            ("Gadag", "Gadag"),
            ("Udupi", "Udupi"),
            ("Robertsonpet", "Robertsonpet"),
            ("Bhadravati", "Bhadravati"),
            ("Chitradurga", "Chitradurga"),
            ("Harihar", "Harihar"),
            ("Kolar", "Kolar"),
            ("Mandya", "Mandya"),
            ("Chikkamagallooru", "Chikkamagallooru"),
            ("Chikmagalur", "Chikmagalur"),
            ("Gangawati", "Gangawati"),
            ("Ranebennuru", "Ranebennuru"),
            ("Ramanagara", "Ramanagara"),
            ("Bagalkot", "Bagalkot"),
        ),
    ),
    (
        "Kerala",
        (
            ("Thiruvananthapuram", "Thiruvananthapuram"),
            ("Kochi", "Kochi"),
            ("Calicut", "Calicut"),
            ("Kollam", "Kollam"),
            ("Thrissur", "Thrissur"),
            ("Kannur", "Kannur"),
            ("Kasaragod", "Kasaragod"),
            ("Alappuzha", "Alappuzha"),
            ("Alappuzha", "Alappuzha"),
            ("Palakkad", "Palakkad"),
            ("Kottayam", "Kottayam"),
            ("Kothamangalam", "Kothamangalam"),
            ("Malappuram", "Malappuram"),
            ("Manjeri", "Manjeri"),
            ("Thalassery", "Thalassery"),
            ("Ponnani", "Ponnani"),
        ),
    ),
    ("Lakshadweep", (("Kavaratti", "Kavaratti"),),),
    (
        "Maharashtra",
        (
            ("Mumbai", "Mumbai"),
            ("Pune", "Pune"),
            ("Nagpur", "Nagpur"),
            ("Nashik", "Nashik"),
            ("Pimpri-Chinchwad", "Pimpri-Chinchwad"),
            ("Aurangabad", "Aurangabad"),
            ("Solapur", "Solapur"),
            ("Bhiwandi", "Bhiwandi"),
            ("Amravati", "Amravati"),
            ("Nanded", "Nanded"),
            ("Kolhapur", "Kolhapur"),
            ("Sangli-Miraj-Kupwad", "Sangli-Miraj-Kupwad"),
            ("Jalgaon", "Jalgaon"),
            ("Akola", "Akola"),
            ("Latur", "Latur"),
            ("Malegaon", "Malegaon"),
            ("Dhule", "Dhule"),
            ("Ahmednagar", "Ahmednagar"),
            ("Nandurbar", "Nandurbar"),
            ("Ichalkaranji", "Ichalkaranji"),
            ("Chandrapur", "Chandrapur"),
            ("Jalna", "Jalna"),
            ("Parbhani", "Parbhani"),
            ("Bhusawal", "Bhusawal"),
            ("Satara", "Satara"),
            ("Beed", "Beed"),
            ("Pandharpur", "Pandharpur"),
            ("Yavatmal", "Yavatmal"),
            ("Kamptee", "Kamptee"),
            ("Gondia", "Gondia"),
            ("Achalpur", "Achalpur"),
            ("Osmanabad", "Osmanabad"),
            ("Hinganghat", "Hinganghat"),
            ("Wardha", "Wardha"),
            ("Barshi", "Barshi"),
            ("Chalisgaon", "Chalisgaon"),
            ("Amalner", "Amalner"),
            ("Khamgaon", "Khamgaon"),
            ("Akot", "Akot"),
            ("Udgir", "Udgir"),
            ("Bhandara", "Bhandara"),
            ("Parli", "Parli"),
        ),
    ),
    ("Meghalaya", (("Shillong", "Shillong"),),),
    ("Manipur", (("Imphal", "Imphal"),),),
    (
        "Madhya Pradesh",
        (
            ("Indore", "Indore"),
            ("Bhopal", "Bhopal"),
            ("Jabalpur", "Jabalpur"),
            ("Gwalior", "Gwalior"),
            ("Ujjain", "Ujjain"),
            ("Sagar", "Sagar"),
            ("Dewas", "Dewas"),
            ("Satna", "Satna"),
            ("Ratlam", "Ratlam"),
            ("Rewa", "Rewa"),
            ("Katni", "Katni"),
            ("Singrauli", "Singrauli"),
            ("Burhanpur", "Burhanpur"),
            ("Khandwa", "Khandwa"),
            ("Morena", "Morena"),
            ("Bhind", "Bhind"),
            ("Chhindwara", "Chhindwara"),
            ("Guna", "Guna"),
            ("Shivpuri", "Shivpuri"),
            ("Vidisha", "Vidisha"),
            ("Chhatarpur", "Chhatarpur"),
            ("Damoh", "Damoh"),
            ("Mandsaur", "Mandsaur"),
            ("Khargone", "Khargone"),
            ("Neemuch", "Neemuch"),
            ("Pithampur", "Pithampur"),
            ("Hoshangabad", "Hoshangabad"),
            ("Itarsi", "Itarsi"),
            ("Sehore", "Sehore"),
            ("Betul", "Betul"),
            ("Seoni", "Seoni"),
            ("Datia", "Datia"),
            ("Nagda", "Nagda"),
            ("Dhanpuri", "Dhanpuri"),
            ("Dhar", "Dhar"),
            ("Balaghat", "Balaghat"),
        ),
    ),
    ("Mizoram", (("Aizawl", "Aizawl"),),),
    ("Nagaland", (("Dimapur", "Dimapur"), ("Kohima", "Kohima"),),),
    (
        "Odisha",
        (
            ("Bhubaneswar", "Bhubaneswar"),
            ("Cuttack", "Cuttack"),
            ("Rourkela", "Rourkela"),
            ("Berhampur", "Berhampur"),
            ("Sambalpur", "Sambalpur"),
            ("Puri", "Puri"),
            ("Balasore", "Balasore"),
            ("Bhadrak", "Bhadrak"),
            ("Baripada", "Baripada"),
            ("Balangir", "Balangir"),
            ("Jharsuguda", "Jharsuguda"),
            ("Jeypore", "Jeypore"),
        ),
    ),
    (
        "Punjab",
        (
            ("Ludhiana", "Ludhiana"),
            ("Amritsar", "Amritsar"),
            ("Jalandhar", "Jalandhar"),
            ("Patiala", "Patiala"),
            ("Bathinda", "Bathinda"),
            ("Hoshiarpur", "Hoshiarpur"),
            ("Batala", "Batala"),
            ("Mohali", "Mohali"),
            ("Abohar", "Abohar"),
            ("Pathankot", "Pathankot"),
            ("Moga", "Moga"),
            ("Malerkotla", "Malerkotla"),
            ("Khanna", "Khanna"),
            ("Muktasar", "Muktasar"),
            ("Barnala", "Barnala"),
            ("Firozpur", "Firozpur"),
            ("Kapurthala", "Kapurthala"),
            ("Phagwara", "Phagwara"),
            ("Zirakpur", "Zirakpur"),
            ("Rajpura", "Rajpura"),
        ),
    ),
    (
        "Puducherry",
        (
            ("Pondicherry", "Pondicherry"),
            ("Ozhukarai", "Ozhukarai"),
            ("Karaikal", "Karaikal"),
        ),
    ),
    (
        "Rajasthan",
        (
            ("Jaipur", "Jaipur"),
            ("Jodhpur", "Jodhpur"),
            ("Kota", "Kota"),
            ("Bikaner", "Bikaner"),
            ("Ajmer", "Ajmer"),
            ("Udaipur", "Udaipur"),
            ("Bhilwara", "Bhilwara"),
            ("Alwar", "Alwar"),
            ("Bharatpur", "Bharatpur"),
            ("Sri Ganganagar", "Sri Ganganagar"),
            ("Sikar", "Sikar"),
            ("Pali", "Pali"),
            ("Barmer", "Barmer"),
            ("Tonk", "Tonk"),
            ("Kishangarh", "Kishangarh"),
            ("Chittorgarh", "Chittorgarh"),
            ("Beawar", "Beawar"),
            ("Hanumangarh", "Hanumangarh"),
            ("Dholpur", "Dholpur"),
            ("Gangapur", "Gangapur"),
            ("Sawai Madhopur", "Sawai Madhopur"),
            ("Churu", "Churu"),
            ("Baran", "Baran"),
            ("Makrana", "Makrana"),
            ("Nagaur", "Nagaur"),
            ("Hindaun", "Hindaun"),
            ("Bhiwadi", "Bhiwadi"),
            ("Bundi", "Bundi"),
            ("Sujangarh", "Sujangarh"),
            ("Jhunjhunu", "Jhunjhunu"),
            ("Banswara", "Banswara"),
            ("Sardarshahar", "Sardarshahar"),
            ("Fatehpur", "Fatehpur"),
            ("Dausa", "Dausa"),
            ("Karauli", "Karauli"),
        ),
    ),
    ("Sikkim", (("Gangtok", "Gangtok"),),),
    (
        "Telangana",
        (
            ("Hyderabad", "Hyderabad"),
            ("Warangal", "Warangal"),
            ("Nizamabad", "Nizamabad"),
            ("Karimnagar", "Karimnagar"),
            ("Ramagundam", "Ramagundam"),
            ("Khammam", "Khammam"),
            ("Mahbubnagar", "Mahbubnagar"),
            ("Nalgonda", "Nalgonda"),
            ("Adilabad", "Adilabad"),
            ("Siddipet", "Siddipet"),
            ("Suryapet", "Suryapet"),
            ("Miryalaguda", "Miryalaguda"),
            ("Jagtial", "Jagtial"),
            ("Mancherial", "Mancherial"),
            ("Kothagudem", "Kothagudem"),
        ),
    ),
    (
        "Tamil Nadu",
        (
            ("Chennai", "Chennai"),
            ("Coimbatore", "Coimbatore"),
            ("Madurai", "Madurai"),
            ("Tiruchirappalli", "Tiruchirappalli"),
            ("Tirupur", "Tirupur"),
            ("Salem", "Salem"),
            ("Erode", "Erode"),
            ("Tirunelveli", "Tirunelveli"),
            ("Vellore", "Vellore"),
            ("Tuticorin", "Tuticorin"),
            ("Gudiyatham", "Gudiyatham"),
            ("Nagercoil", "Nagercoil"),
            ("Thanjavur", "Thanjavur"),
            ("Dindigul", "Dindigul"),
            ("Vaniyambadi", "Vaniyambadi"),
            ("Cuddalore", "Cuddalore"),
            ("Komarapalayam", "Komarapalayam"),
            ("Kanchipuram", "Kanchipuram"),
            ("Ambur", "Ambur"),
            ("Tiruvannamalai", "Tiruvannamalai"),
            ("Pudukkottai", "Pudukkottai"),
            ("Kumbakonam", "Kumbakonam"),
            ("Rajapalayam", "Rajapalayam"),
            ("Hosur", "Hosur"),
            ("Karaikudi", "Karaikudi"),
            ("Neyveli", "Neyveli"),
            ("Nagapattinam", "Nagapattinam"),
            ("Viluppuram", "Viluppuram"),
            ("Paramakudi", "Paramakudi"),
            ("Tiruchengode", "Tiruchengode"),
            ("Kovilpatti", "Kovilpatti"),
            ("Theni-Allinagaram", "Theni-Allinagaram"),
            ("Kadayanallur", "Kadayanallur"),
            ("Pollachi", "Pollachi"),
            ("Ooty", "Ooty"),
        ),
    ),
    ("Tripura", (("Agartala", "Agartala"),),),
    (
        "Uttar Pradesh",
        (
            ("Kanpur", "Kanpur"),
            ("Lucknow", "Lucknow"),
            ("Ghaziabad", "Ghaziabad"),
            ("Agra", "Agra"),
            ("Varanasi", "Varanasi"),
            ("Meerut", "Meerut"),
            ("Allahabad", "Allahabad"),
            ("Bareilly", "Bareilly"),
            ("Aligarh", "Aligarh"),
            ("Moradabad", "Moradabad"),
            ("Saharanpur", "Saharanpur"),
            ("Gorakhpur", "Gorakhpur"),
            ("Faizabad", "Faizabad"),
            ("Firozabad", "Firozabad"),
            ("Jhansi", "Jhansi"),
            ("Muzaffarnagar", "Muzaffarnagar"),
            ("Mathura", "Mathura"),
            ("Budaun", "Budaun"),
            ("Rampur", "Rampur"),
            ("Shahjahanpur", "Shahjahanpur"),
            ("Farrukhabad", "Farrukhabad"),
            ("Mau", "Mau"),
            ("Hapur", "Hapur"),
            ("Noida", "Noida"),
            ("Etawah", "Etawah"),
            ("Mirzapur", "Mirzapur"),
            ("Bulandshahr", "Bulandshahr"),
            ("Sambhal", "Sambhal"),
            ("Amroha", "Amroha"),
            ("Hardoi", "Hardoi"),
            ("Fatehpur", "Fatehpur"),
            ("Raebareli", "Raebareli"),
            ("Orai", "Orai"),
            ("Sitapur", "Sitapur"),
            ("Bahraich", "Bahraich"),
            ("Modinagar", "Modinagar"),
            ("Unnao", "Unnao"),
            ("Jaunpur", "Jaunpur"),
            ("Lakhimpur", "Lakhimpur"),
            ("Hathras", "Hathras"),
            ("Banda", "Banda"),
            ("Pilibhit", "Pilibhit"),
            ("Barabanki", "Barabanki"),
            ("Mughalsarai", "Mughalsarai"),
            ("Khurja", "Khurja"),
            ("Gonda", "Gonda"),
            ("Mainpuri", "Mainpuri"),
            ("Lalitpur", "Lalitpur"),
            ("Etah", "Etah"),
            ("Deoria", "Deoria"),
            ("Ujhani", "Ujhani"),
            ("Ghazipur", "Ghazipur"),
            ("Sultanpur", "Sultanpur"),
            ("Azamgarh", "Azamgarh"),
            ("Bijnor", "Bijnor"),
            ("Sahaswan", "Sahaswan"),
            ("Basti", "Basti"),
            ("Chandausi", "Chandausi"),
            ("Akbarpur", "Akbarpur"),
            ("Ballia", "Ballia"),
            ("Mubarakpur", "Mubarakpur"),
            ("Tanda", "Tanda"),
            ("Greater Noida", "Greater Noida"),
            ("Shikohabad", "Shikohabad"),
            ("Shamli", "Shamli"),
            ("Baraut", "Baraut"),
            ("Khair", "Khair"),
            ("Kasganj", "Kasganj"),
            ("Auraiya", "Auraiya"),
            ("Khatauli", "Khatauli"),
            ("Deoband", "Deoband"),
            ("Nagina", "Nagina"),
            ("Mahoba", "Mahoba"),
            ("Muradnagar", "Muradnagar"),
            ("Bhadohi", "Bhadohi"),
            ("Dadri", "Dadri"),
            ("Pratapgarh", "Pratapgarh"),
            ("Najibabad", "Najibabad"),
        ),
    ),
    (
        "Uttarakhand",
        (
            ("Dehradun", "Dehradun"),
            ("Haridwar", "Haridwar"),
            ("Roorkee", "Roorkee"),
            ("Haldwani", "Haldwani"),
            ("Rudrapur", "Rudrapur"),
            ("Kashipur", "Kashipur"),
            ("Rishikesh", "Rishikesh"),
        ),
    ),
    (
        "West Bengal",
        (
            ("Kolkata", "Kolkata"),
            ("Asansol", "Asansol"),
            ("Siliguri", "Siliguri"),
            ("Durgapur", "Durgapur"),
            ("Bardhaman", "Bardhaman"),
            ("Malda", "Malda"),
            ("Baharampur", "Baharampur"),
            ("Habra", "Habra"),
            ("Jalpaiguri", "Jalpaiguri"),
            ("Kharagpur", "Kharagpur"),
            ("Shantipur", "Shantipur"),
            ("Dankuni", "Dankuni"),
            ("Dhulian", "Dhulian"),
            ("Ranaghat", "Ranaghat"),
            ("Haldia", "Haldia"),
            ("Raiganj", "Raiganj"),
            ("Krishnanagar", "Krishnanagar"),
            ("Nabadwip", "Nabadwip"),
            ("Midnapore", "Midnapore"),
            ("Balurghat", "Balurghat"),
            ("Basirhat", "Basirhat"),
            ("Bankura", "Bankura"),
            ("Chakdaha", "Chakdaha"),
            ("Darjeeling", "Darjeeling"),
            ("Alipurduar", "Alipurduar"),
            ("Purulia", "Purulia"),
            ("Jangipur", "Jangipur"),
            ("Bangaon", "Bangaon"),
            ("Cooch Behar", "Cooch Behar"),
            ("Bolpur", "Bolpur"),
            ("Kanthi", "Kanthi"),
        ),
    ),
)

   




    State_Name = models.CharField(max_length = 255, choices=STATES)
    City_Name = models.CharField(max_length = 255, choices=cities)
    Hotel_Name = models.CharField(max_length=255)
    Hotel_Type = models.CharField(max_length=255,choices=TYPE_CHOICES)
    Image_1 = models.ImageField(null = True, blank = True)

    Image_2 = models.ImageField(null = True, blank = True)

    
    def __str__(self):
        return self.Hotel_Type




