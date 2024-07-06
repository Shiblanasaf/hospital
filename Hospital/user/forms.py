from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from.models import Medicine,Staff


class PatientForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    place=forms.CharField(max_length=100)
    phone=forms.IntegerField()
    email=forms.EmailField()
    def clean(self) -> dict[str, Any]:
        cleaned_data=super().clean()
        age=cleaned_data.get('age')
        if age<=0:
            self.add_error("age","age must be greater than 0!")
        
        return cleaned_data


class DoctorForm(forms.Form):
    first_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Firstname"}))
    last_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Laststname"}))
    phone=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter Phonenumber"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Enter Email"}))
    dept=forms.CharField(max_length=100,label="Department",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Department"}))

    def clean(self):
        data=super().clean()
        print(data)
        ph=data.get('phone')
        if len(str(ph))!=10:
           self.add_error("phone","phone number  must be 10 digits!")
        return data
    

class MedicineForm(forms.ModelForm):
    class Meta:
        model=Medicine
        fields="__all__"
        widgets={
            "mname":forms.TextInput(attrs={"class":"form-control","placeholder":"enter a medicine name"}),
            "price":forms.NumberInput(attrs={"class":"form-control","placeholder":"enter medicine price"}),
            "expiry_date":forms.DateInput(attrs={"class":"form-control","placeholder":"enter expiry date"}),
            "pharma_company":forms.TextInput(attrs={"class":"form-control","placeholder":"enter company name"})
        }

class StaffForm(forms.ModelForm):
    class Meta:
        model=Staff
        fields="__all__"  
        widgets={
            "fname":forms.TextInput(attrs={"class":"form-control","placeholder":"enter firstname"}),
            "lname":forms.TextInput(attrs={"class":"form-control","placeholder":"enter lastname"}),
            "age":forms.NumberInput(attrs={"class":"form-control","placeholder":"enter age"}),
            "phone":forms.NumberInput(attrs={"class":"form-control","placeholder":"enter phone number"}),
            "email":forms.EmailInput(attrs={"class":"form-control","placeholder":"enter email"}),
            "designation":forms.TextInput(attrs={"class":"form-control","placeholder":"enter designation"})

        }

    







