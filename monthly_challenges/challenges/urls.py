from . import views
from django.urls import path,include

urlpatterns = [
   
    path("<int:month>",views.monthly_challenge_by_number),
    path("<str:month>",views.monthly_challenge,name="month-challenge")
]
