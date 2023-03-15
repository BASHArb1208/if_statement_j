from django.shortcuts import render

# Create your views here.
def tata(request):
    d={'a':50}
    return render(request,'tata.html',d)
