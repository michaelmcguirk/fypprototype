from django.shortcuts import render

from django.http import HttpResponse
from .models import CurrentTemp

def index(request):
	return HttpResponse(CurrentTemp.objects.all())

# Create your views here.
