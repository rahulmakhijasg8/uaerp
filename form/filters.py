import django_filters
from .models import EntryForm

class DataFilter(django_filters.FilterSet):
    class Meta:
        model = EntryForm
        fields = ['State_Name','City_Name','Hotel_Type']