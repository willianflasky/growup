from django.forms import ModelForm,forms


#
# class CustomerForm(ModelForm):
#     def __new__
#     class Meta:
#         model = models.Customer
#         fields = "__all__"
#       def clean():

# class CourseForm(ModelForm):
#
#     class Meta:
#         model = models.Course
#         fields = "__all__"


def __new__(cls, *args, **kwargs):
    print(cls.base_fields)
    for field_name in cls.base_fields:
        field = cls.base_fields[field_name]
        #print("field", field)
        # print("field repr",field_name,field.__repr__())
        attr_dic = { 'class': 'form-control'}
        if field_name in cls.admin_class.readonly_fields:
            attr_dic['disabled'] = True
        field.widget.attrs.update(attr_dic)

    return ModelForm.__new__(cls)

def create_dynamic_modelform(model_class,admin_class):

    class Meta:
        model = model_class
        fields = "__all__"


    def default_clean(self):
        # print("self.errors ",self.errors )
        print("clean::::",self.cleaned_data)
        for field in  self.admin_class.readonly_fields:
            if hasattr(self.instance,field):
                field_val_in_db = getattr(self.instance,field)
                new_val = self.cleaned_data.get(field)
                field_type = self.instance._meta.get_field(field).get_internal_type()
                if field_type == "ManyToManyField":
                    field_val_in_db = field_val_in_db.all()

                    field_val_in_db = [obj.id for obj in field_val_in_db]
                    new_val = [obj.id for obj in new_val]
                if field_val_in_db != new_val: #data got changed by web page
                    self.add_error(field , "Readonly Field: field should be '{value}' ,not '{new_value}' ". \
                                   format(**{'value': field_val_in_db, 'new_value': new_val}))


            else:
                raise forms.ValidationError(("This field doesn't exist in form but been set in readonly_fields."))

    dynamic_modelform = type("DynamicModelForm",
                             (ModelForm,),
                             {'Meta':Meta,'__new__':__new__,
                              'clean':default_clean,
                              'admin_class':admin_class

                             # 'clean_consultant':clean_consultant,
                              })
    return dynamic_modelform
    #form_obj = dynamic_modelform(instance=model_obj)


