from django.shortcuts import render

# Create your views here.
def homepageView(request):
    return render(request, "homepage/homepage.html")