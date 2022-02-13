from django.views.generic import TemplateView
from products.models import Product
from django.shortcuts import render

# def mainPage(request):
#     return render(request, 'home/home.html', {})

class MainPageView(TemplateView):
    template_name='home/home.html'
    model = Product
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lst = Product.objects.all().order_by('-created')[:9]
        context.update({'lst': lst})
        return context

def views_404(request, exception=None):
    return render(request, 'home/404.html')
