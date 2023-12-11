from django.shortcuts import render

# Create your views here.
def login(request):

    d={'UserName':'Rojalin'}
    return render(request,'login.html',context=d)