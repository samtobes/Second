from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from .models import News,Subscribers
from django.http import HttpResponse

def home(request):
    if request.method == "POST": 
        input_email= request.POST.get("email")
        if not Subscribers.objects.filter(email=input_email).exists():
            Subscribers.objects.create(email=input_email)
            return redirect(reverse("home"))
        else:
            return HttpResponse("Email address is taken")
    elif request.method == "GET":
        all_news = News.objects.all()
        context = {"all_news":all_news}
        return render(request,"index.html",context)
       
def detail(request,slug):
    current_news = get_object_or_404(News,slug=slug)
    context = {"current_news":current_news}
    return render(request,"single-post.html",context)