from django.shortcuts import render,get_object_or_404
from bands.models import Musician
from django.core.paginator import Paginator

# Create your views here.

def musician(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id)
    data = {
        "musician": musician,
    }

    return render(request,"musician.html",data)

def musicians(request):
    all_musicians = Musician.objects.all().order_by('first_name')
    paginator = Paginator(all_musicians,2)
    
    page_num = int(request.GET.get('page',1))
    
    if page_num < 1:
        page_num = 1
    elif page_num > paginator.num_pages:
        page_num = paginator.num_pages
    
    page = paginator.page(page_num)
    
    data = {
        "musicians": page.object_list,
        "page": page,
    }
        
    
    
    return render(request,"musicians.html",data)