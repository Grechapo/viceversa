# from django.http import HttpResponse
from django.shortcuts import render




# def home(request):
#     return HttpResponse('trytrytry')


def home(request):
    return render(request, 'home.html')




