from django.shortcuts import render


from django.views.generic import TemplateView

from .models import Product, Category
from django.views.generic import ListView
# Create your views here.


def home(request):
    return render(request, 'store/home.html')

class HomeView(TemplateView):
    template_name = 'store/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Welcome to the E-commerce Store!',
        context['products'] = Product.objects.all()
        context['categories'] = Category.objects.all()
        return context