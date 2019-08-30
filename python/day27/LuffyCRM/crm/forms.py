
from django import forms
from crm import models



class CustomerForm(forms.ModelForm):
    class Meta:
        model = models.Customer
        fields = '__all__'

    def clean_phone(self): #单个字段的验证
        print("clean qq:weixin phone ",self.cleaned_data)

    def clean(self):
        print("clean data",self.cleaned_data)
        if self.cleaned_data.get('phone') or self.cleaned_data.get('weixin') or self.cleaned_data.get('qq'):
            print("passs validation")
        else:
            raise forms.ValidationError("phone,weixin.qq至少三选一")