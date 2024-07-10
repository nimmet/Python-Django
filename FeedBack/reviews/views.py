from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForrm


# Create your views here.


def review(request):
    entered_username=""
    if request.method == 'POST':
        form = ReviewForrm(request.POST)
        
        if form.is_valid():
            return HttpResponseRedirect("/thank-you")
        
    else:
        form = ReviewForrm()
        
    return render(request, "reviews/review.html", {
        "form": form,
    })


def thank_you(request):
    return render(request,"reviews/thank_you.html")