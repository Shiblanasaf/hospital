from django.shortcuts import render,redirect
from django.views import View
from .forms import PatientForm,DoctorForm,MedicineForm,StaffForm
from django.http import HttpResponse
from .models import Patient
from .models import Doctor,Medicine,Staff
from django .contrib import messages


# Create your views here.

class UserHomeView(View):
    def get(self,request):
        return render(request,"userhome.html")
    

class PatientView(View):
    def get(self,request):
        form=PatientForm()
        return render(request,"regpatient.html",{"form":form})
    def post(self,request):
        form_data=PatientForm(data=request.POST)
        if form_data.is_valid():
            name=form_data.cleaned_data.get('name')
            ag=form_data.cleaned_data.get('age')
            ph=form_data.cleaned_data.get('phone')
            pl=form_data.cleaned_data.get('place')
            em=form_data.cleaned_data.get('email')
            Patient.objects.create(name=name,age=ag,phone=ph,place=pl,email=em)
            return redirect('uhome')
        print(form_data.errors)
        return  render(request,"regpatient.html",{"form":form_data})
    

class DoctorView(View):
    def get(self,request):
        form=DoctorForm()
        return render(request,"doctorreg.html",{"form":form})
    def post(self,request):
        form_data=DoctorForm(data=request.POST)
        if form_data.is_valid():
            fname=form_data.cleaned_data.get('first_name')
            lname=form_data.cleaned_data.get('last_name')
            em=form_data.cleaned_data.get('email')
            ph=form_data.cleaned_data.get('phone')
            dpt=form_data.cleaned_data.get('dept')
            # print(fname,lname,em,ph,dpt)
            # return HttpResponse("Submitted")
            Doctor.objects.create(fname=fname,lname=lname,phone=ph,email=em,dept=dpt)
            return redirect('uhome')
        print(form_data.errors)
        return  render(request,"doctorreg.html",{"form":form_data})
    





class PatientListView(View):
    def get(self,request):
        data=Patient.objects.all
        print(data)
        return render(request,"patientlist.html",{"patients":data})
    

class DoctorListView(View):
    def get(self,request):
        data=Doctor.objects.all
        print(data)
        return render(request,"doclist.html",{"doc":data})
    

class PatientRemoveView(View):
    def get(self,request,*args,**kwargs):
    
    
        pid=kwargs.get('pid')
        pat=Patient.objects.get(id=pid)
        pat.delete()
        return redirect('plist')
        


class DoctorRemoveView(View):
    def get(self,request,*args,**kwargs):
        # print(kwargs.get('did'))
        # return HttpResponse("id shared")
        did=kwargs.get('did')
        doc=Doctor.objects.get(id=did)
        doc.delete()
        return redirect('doclist')
    

class EditPatientView(View):
    def get(self,request,**kwargs):
        pid=kwargs.get("pid")
        print(pid)
        pat=Patient.objects.get(id=pid)
        form=PatientForm(initial={"name":pat.name,"age":pat.age,"place":pat.place,"phone":pat.phone,"email":pat.email})
        return render(request,"editpat.html",{"form":form})
    

    def post(self,request,**kwargs):
        pid=kwargs.get('pid')
        pat=Patient.objects.get(id=pid)
        form_data=PatientForm(data=request.POST)
        if form_data.is_valid():
            nm=form_data.cleaned_data.get('name')
            ag=form_data.cleaned_data.get('age')
            pl=form_data.cleaned_data.get('place')
            ph=form_data.cleaned_data.get('phone')
            em=form_data.cleaned_data.get('email')
            pat.name=nm
            pat.age=ag
            pat.place=pl
            pat.phone=ph
            pat.email=em
            pat.save()
            return redirect("plist")
        return render(request,"editpat.html",{"form":form_data})
    


        
class EditDoctorView(View):
    def get(self,request,**kwargs):
        did=kwargs.get("did")
        print(did)
        doc=Doctor.objects.get(id=did)
        form=DoctorForm(initial={"fname":doc.fname,"lname":doc.lname,"phone":doc.phone,"email":doc.email,"dpt":"dept"})
        return render(request,"editdoc.html",{"form":form})
    

    def post(self,request,**kwargs):
        did=kwargs.get("did")
        doc=Doctor.objects.get(id=did)
        form_data=DoctorForm(data=request.POST)
        if form_data.is_valid():
            fname=form_data.cleaned_data.get('first_name')
            lname=form_data.cleaned_data.get('last_name')
            ph=form_data.cleaned_data.get('phone')
            em=form_data.cleaned_data.get('email')
            dpt=form_data.cleaned_data.get("dept")
            doc.fname=fname
            doc.lname=lname
            doc.phone=ph
            doc.email=em
            doc.dept=dpt
            doc.save()
            return redirect("doclist")
        return render(request,"editdoc.html",{"form":form_data})
    


class MedicineView(View):
    def get(self,request):
        form=MedicineForm()
        return render(request,"addmed.html",{"form":form})
    


    def post(self,request):
    
        # print(request.FILES)

        form_data=MedicineForm(data=request.POST,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"medicine added succesfully")
            return redirect('medlist')
        messages.error(request,"medicine adding failed")
        return render(request,"addmed.html",{"form":form_data})
    
class MedicineListView(View):
    def get(self,request):
        data=Medicine.objects.all()
        print(data)
        return render(request,"medlist.html",{"med":data})
    
    

class MedicineRemoveView(View):
    def get(self,request,*args,**kwargs):
        try:
            mid=kwargs.get('mid')
            med=Medicine.objects.get(id=mid)
            med.delete()
            messages.success(request,"Medicine deleted succesfully")
            return redirect('medlist')
        except:
            messages.error(request,"medicine deletion failed")
            return redirect('medlist')
    


class MedicineEditView(View):
    def get(self,request,*args,**kwargs):
        mid=kwargs.get('mid')
        med=Medicine.objects.get(id=mid)
        # form=MedicineForm()
        form=MedicineForm(instance=med)
        return render(request,"editmed.html",{"form":form})
    


    def post(self,request,**kwargs):
        mid=kwargs.get('mid')
        med=Medicine.objects.get(id=mid)
        form_data=MedicineForm(data=request.POST,instance=med,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect('medlist')
        return render(request,"editmed.html",{"form":form_data})


class StaffView(View):
    def get(self,request):
        form=StaffForm()
        return render(request,"staffreg.html",{"form":form})
    
    def post(self,request):
    
        # print(request.FILES)

        form_data=StaffForm(data=request.POST,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"staff added succesfully")
            return redirect('medlist')
        messages.error(request,"staff adding failed")
        return render(request,"staffreg.html",{"form":form_data})
    
class StaffListView(View):
    def get(self,request):
        data=Staff.objects.all()
        print(data)
        return render(request,"stafflist.html",{"staff":data})
    
    

class StaffRemoveView(View):
    def get(self,request,*args,**kwargs):
        try:
            sid=kwargs.get('sid')
            staff=Staff.objects.get(id=sid)
            staff.delete()
            messages.success(request,"Staff deleted succesfully")
            return redirect('stafflist')
        except:
            messages.error(request,"staff deletion failed")
            return redirect('stafflist')
    


class StaffEditView(View):
    def get(self,request,*args,**kwargs):
        sid=kwargs.get('sid')
        staff=Staff.objects.get(id=sid)
        # form=staffForm()
        form=StaffForm(instance=staff)
        return render(request,"editstaff.html",{"form":form})
    


    def post(self,request,**kwargs):
        sid=kwargs.get('sid')
        staff=Staff.objects.get(id=sid)
        form_data=StaffForm(data=request.POST,instance=staff,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            return redirect('stafflist')
        return render(request,"editstaff.html",{"form":form_data})


    




    


    








    
    
