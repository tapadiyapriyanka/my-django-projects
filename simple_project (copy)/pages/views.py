from django.shortcuts import render
<<<<<<< HEAD
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'
=======
from django.http import HttpResponse

# Create your views here.
def homePageView(request):
    return HttpResponse('Hello, Priyanka..........!\n Congrates!!!!!!!!!(:')
>>>>>>> 171f531816a2bab6ba61924e93f9b7a677a82750
