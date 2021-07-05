from django.urls import path, include
from .views import *

urlpatterns = [
     path('create/',create_employee, name='create/employee' ),
     path('get/', get_allrecord, name='get_allrecord'),
     path('update/', update_record),
     path('delete/', delete_record),
     path('filter/', get_filter, name= 'filterrecord')
]