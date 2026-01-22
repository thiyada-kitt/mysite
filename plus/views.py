from django.shortcuts import render

# Create your views here.
def home(request):
    # process the request and return a response
    return render(request, 'plus/home.html')