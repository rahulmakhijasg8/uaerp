from django import forms
from .models import EntryForm
  
class entryForm(forms.ModelForm):
    class Meta:
        model = EntryForm
        fields = "__all__"


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)