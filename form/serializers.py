from django.db.models import fields
from rest_framework import serializers
from . models import Hotelinfo

class Hotelinfoserializer(serializers.ModelSerializer):
    class Meta:
        model = Hotelinfo
        fields = "__all__"
        

