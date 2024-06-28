from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Lerne Deautsch, es it wichtig!",
    "april": "Raus, das  wetter is seher gut",
    "may": "Walk for at least 20 minutes every day!",
    "june": "gehe ins schwimmbad",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Lerne Deautsch, es it wichtig!",
    "october": "Raus, das  wetter is seher gut",
    "november": "Walk for at least 20 minutes every day!",
    "december": "gehe ins schwimmbad"
}

def index(request):
    
    list_items = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def feb(request):
    return  HttpResponse("Febuary challenges here!")

def monday(request):
    return HttpResponse("Montag ist lustig")


# def monthly_challenge_by_number(request, month):
#     match month:
#         case "1":
#             challenge_text = "Eat no meat for the entire month!"
#         case "2":
#             challenge_text = "Walk for at least 20 minutes every day!"
#         case "3":
#             challenge_text = "Lerne Deautsch, es it wichtig!"
#         case "4":
#             challenge_text = "Raus, das  wetter is seher gut"
#         case _:
#             return HttpResponseNotFound("Es gibt etwas fehler")
#     return HttpResponse(challenge_text)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid number of monthly challenges")
        
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    
    

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month] 
        response_data  = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)   
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")    
    