from django.shortcuts import render

# Create your views here.
def ifblock(request):
    d={'a':10,'b':15,'c':12}
    return render(request,'ifblock.html',d)