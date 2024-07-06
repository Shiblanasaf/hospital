from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('uhome',UserHomeView.as_view(),name="uhome"),
    path('addpat',PatientView.as_view(),name="addpat"),
    path('docreg',DoctorView.as_view(),name="docreg"),
    path('staffreg',StaffView.as_view(),name="staffreg"),
    path('plist',PatientListView.as_view(),name="plist"),
    path('doclist',DoctorListView.as_view(),name="doclist"),
    path('stafflist',StaffListView.as_view(),name="stafflist"),
    path('patdel/<int:pid>',PatientRemoveView.as_view(),name="pdel"),
    path('docdel/<int:did>',DoctorRemoveView.as_view(),name="ddel"),
    path('editpat/<int:pid>',EditPatientView.as_view(),name="epat"),
    path('editdoc/<int:did>',EditDoctorView.as_view(),name="edoc"),
    path('addmed',MedicineView.as_view(),name="addmed"),
    path('meddel/<int:mid>',MedicineRemoveView.as_view(),name="mdel"),
    path('medlist',MedicineListView.as_view(),name="medlist"),
    path('editmed/<int:mid>',MedicineEditView.as_view(),name="emed"),
    path('editstaff/<int:sid>',StaffEditView.as_view(),name="estaff"),
    path('staffdel/<int:sid>',StaffRemoveView.as_view(),name="staffdel")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)