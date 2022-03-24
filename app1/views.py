from django.shortcuts import render

# Create your views here.
def function(request):
    d={'name':'pranay'}
    return render(request,'hari.html',d)

def fun(request):
    d1={'a':95}
    return render(request,'pranay.html',d1)
