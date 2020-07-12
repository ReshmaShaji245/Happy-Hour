from django.shortcuts import render
from django.http import HttpResponse
from .forms import InterestForm
import http.client
# Create your views here.
def contact(request):

    if request.method=="POST":
        form=InterestForm(request.POST)
        if form.is_valid():
            interests=form.cleaned_data['interests']
            hobbies=form.cleaned_data['hobbies']
            genres=form.cleaned_data['genres']
            material=form.cleaned_data['material']
            print(interests,hobbies,genres,material)
            conn = http.client.HTTPSConnection("hummingbirdv1.p.rapidapi.com")

            headers = {
                'x-rapidapi-host': "hummingbirdv1.p.rapidapi.com",
                'x-rapidapi-key': "9d98761b39msh902e0f78cc831e3p165f1cjsnae93d1bdacdf"
                }

            conn.request("GET", "/anime/steins-gate", headers=headers)

            res = conn.getresponse()
            data = res.read()

            print(data.decode("utf-8"))


    form=InterestForm()
    return render(request,'form.html',{'form':form})
