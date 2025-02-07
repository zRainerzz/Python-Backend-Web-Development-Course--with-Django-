from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name': 'Ghaith',
        'age': 21,
        'nationality': 'Tunisian',}
    return render(request, 'index.html', context)