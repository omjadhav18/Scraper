from django.shortcuts import render,HttpResponseRedirect
import requests
from bs4 import BeautifulSoup
from .models import Link

def Scrape(request):
    if request.method=="POST":
             site = request.POST.get('site')
             page = requests.get(site)
             soup = BeautifulSoup(page.text,'html.parser')
    
             for link in soup.find_all('a'):
                 link_address = link.get('href')
                 link_name = link.string
                 Link.objects.create(address = link_address,name= link_name)
             
             
             

    data = Link.objects.all()
    context = {
        'data':data,

    }

    return render(request,'myapp/result.html',context)


def Clear(request):
      Link.objects.all().delete()
      return render(request,'myapp/result.html')