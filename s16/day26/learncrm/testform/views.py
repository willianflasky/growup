from django.shortcuts import render

# Create your views here.

# from django import forms
#
# class CustormForm(forms.Form):
#     name = forms.CharField(max_length=64)
#     qq = forms.CharField(max_length=64)
#
# def customerform(request):
#     return render(request,'testform/testform.html',{'form':CustormForm})



from django.forms import ModelForm
from crm import models

class CustomerForm(ModelForm):
    class Meta:
        model = models.Customer
        fields = '__all__'

def customerform(request):
    object = models.Customer.objects.filter(id=1).get()
    form_obj = CustomerForm(instance=object)
    # return render(request, 'testform/testform.html', {'form': CustomerForm})
    return render(request, 'testform/testform.html', {'form': form_obj})
