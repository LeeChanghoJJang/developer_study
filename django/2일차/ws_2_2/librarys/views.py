from django.shortcuts import render

# Create your views here.
def require(request):
    return render(request,'require.html')
