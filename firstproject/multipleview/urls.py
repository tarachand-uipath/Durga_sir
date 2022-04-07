from django.urls import path 
from multipleview import views



urlpatterns = [
    path('first/', views.first_view),
    path('second/', views.second_view), 
    path('third/', views.third_view),
    path('forth/' , views.forth_view),
    
    
   
]