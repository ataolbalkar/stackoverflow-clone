from django.shortcuts import render


# Create your views here.

def baseView(request):
    return render(request, 'questions/base.html')
