from django.shortcuts import render
from django.http import HttpResponse
from .forms import InterestForm
# Create your views here.
def contact(request):

    if request.method=="POST":
        form=InterestForm(request.POST)
        if form.is_valid():
            hobbies=form.cleaned_data['hobbies']
            genres=form.cleaned_data['genres']
            material=form.cleaned_data['material']
            print(hobbies,genres,material)


    form=InterestForm()
    return render(request,'form.html',{'form':form})
