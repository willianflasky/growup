
from django import forms
from crm import models



class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = '__all__'