from django.urls import path
from myapp22.views import medicine,medicine_details,add_medicine,update_medicine,delete_medicine


urlpatterns = [
    # path('index/',  index),
    path('home/', medicine),
    path('med_details/<int:id>',medicine_details,name='medicine_details'),
    path('meds/add/',add_medicine,name='add_medicine'),
    path('med_update/<int:id>',update_medicine,name='update_medicine'),
    path('med_delete/<int:id>',delete_medicine,name='delete_medicine'),
]
