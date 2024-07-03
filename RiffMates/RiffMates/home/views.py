from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

# Create your views here.

def news(request):
    data = {
        'news':[
        "RiffMates now has a news page!",
        "RiffMates has its first web page",
         ],}
    return render(request,"news2.html",data)
    

def home(request):
    return HttpResponse("<h2>Home</h2>")

def credits(request):
    content = "Ricky\nYour name  "
    return HttpResponse(content, content_type='text/plain')

def about(request):
    content = """
    <h2>About Me</h2>
    <p>
    I am Uyghur and I am a python developer.
    </p>
    """
    return HttpResponse(content)

def info_json(request):
     content = {
        "version":"1.0",
        "name":"Music app",
        "author":"Uyghur",
        "date":"2024-09-23"
    }
     return JsonResponse(content)
    

def info(request):
    content = {
        "version":"1.0",
        "name":"Music app",
        "author":"Uyghur",
        "date":"2024-09-23"
    }
    
    information = [f"<h3>{k} : {v}<h3>" for k,v in content.items()]
    
    return HttpResponse(information)