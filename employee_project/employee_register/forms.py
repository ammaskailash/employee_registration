from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
#        fields = '__all__'
        fields = ('fname','lname','ecode','mobile','roles')
        labels = {
            'fname':'First Name',
            'lname': 'Last Name',
            'ecode': 'Employee Code',
            'mobile': 'Contact Number',
            'roles': 'Roles'
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['roles'].empty_label = "Select"
        self.fields['ecode'].required = False