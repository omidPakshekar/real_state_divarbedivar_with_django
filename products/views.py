from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Seller
from django.views.generic import ( ListView, DetailView,
                    TemplateView, CreateView, UpdateView)
from django.views import View
from django.http import HttpResponse
from .forms import FilterProductForm, FroshCreateForm, RhnCreateForm, EjareCreateForm, CompleteCreateForm
from django.core.files import File
from django.conf import settings
from django.contrib.auth.models import User
import os
import urllib

# sellerListView -- motanaseb ba har seller product seller ra namayesh midehad
class SellerListView(ListView):
    template_name='products/list2.html'
    paginate_by = 4
    model = Product
    f = 0
    queryset = Product.objects.all()
    context_object_name = 'object_list'
    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        products = Product.objects.filter(seller = Seller.objects.get(user=self.request.user))
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
        return products

class FroshCreateView(CreateView):
    template_name = 'products/add_frosh.html'
    model = Product
    form_class = FroshCreateForm
    # redirect = 'orders:order-created'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'form':FroshCreateForm})
        return context
    def get(self, request, *args, **kwargs):
        return render(self.request, 'products/add_frosh.html', {'form':FroshCreateForm})

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response

    def form_valid(self, form):
        form_ = form.save(commit=False)
        form_.seller = Seller.objects.get(user= self.request.user)
        form_. type = 'frosh'
        form_.category = Category.objects.get(name='frosh')
        form_.slug = 'frosh'
        form_.parking = form.cleaned_data['parking']
        form_.nastaghi = form.cleaned_data['nastaghi']
        form_.save()
        return render(self.request, 'products/created.html', {})

class VillaCreateView(CreateView):
    template_name = 'products/add_frosh.html'
    model = Product
    form_class = FroshCreateForm
    # redirect = 'orders:order-created'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'form':FroshCreateForm})
        return context
    def get(self, request, *args, **kwargs):
        return render(self.request, 'products/add_frosh.html', {'form':FroshCreateForm})

    def form_valid(self, form):
        form_ = form.save(commit=False)
        form_.seller = Seller.objects.get(user= self.request.user)
        form_. type = 'villa'
        form_.category = Category.objects.get(name='villa')
        form_.slug = 'villa'
        form_.parking = form.cleaned_data['parking']
        form_.nastaghi = form.cleaned_data['nastaghi']
        form_.save()
        return render(self.request, 'products/created.html', {})


class ProjeMaskoniCreateView(CreateView):
    template_name = 'products/add_frosh.html'
    model = Product
    form_class = FroshCreateForm
    # redirect = 'orders:order-created'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'form':FroshCreateForm})
        return context
    def get(self, request, *args, **kwargs):
        return render(self.request, 'products/add_frosh.html', {'form':FroshCreateForm})

    def form_valid(self, form):
        form_ = form.save(commit=False)
        form_.seller = Seller.objects.get(user= self.request.user)
        form_. type = 'proje'
        form_.category = Category.objects.get(name='proje')
        form_.slug = 'proje'
        form_.parking = form.cleaned_data['parking']
        form_.nastaghi = form.cleaned_data['nastaghi']
        form_.save()
        return render(self.request, 'products/created.html', {})

# ********************* rhn ****************************
class RhnCreateView(CreateView):
    template_name = 'products/add_rhn.html'
    model = Product
    form_class = RhnCreateForm

    def form_invalid(self, form):
        print(form.cleaned_data)
        response = super().form_invalid(form)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'form':RhnCreateForm})
        return context
    def get(self, request, *args, **kwargs):
        return render(self.request, 'products/add_rhn.html', {'form':RhnCreateForm})

    def form_valid(self, form):
        print('rhnCreateVIew')
        form_ = form.save(commit=False)
        form_.seller = Seller.objects.get(user= self.request.user)
        form_. type = 'rhn'
        form_.category = Category.objects.get(name='rhn-va-ejare')
        form_.slug = 'rhn'
        form_.parking = form.cleaned_data['parking']
        form_.save()
        return render(self.request, 'products/created.html', {})


class EjareCreateView(CreateView):
    template_name = 'products/add_ejare.html'
    model = Product
    form_class = EjareCreateForm
    # redirect = 'orders:order-created'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'form':EjareCreateForm})
        return context
    def get(self, request, *args, **kwargs):
        return render(self.request, 'products/add_ejare.html', {'form':EjareCreateForm})

    def post(self, request, *args, **kwargs):
        name = self.request.POST['name']
        address = self.request.POST['address']
        parking = False
        _no_parking = None
        _parking = None
        try:
            _parking = self.request.POST['parking']
        except:
            pass
        try:
            _no_parking = self.request.POST['no_parking']
        except:
            pass
        if _parking == 'on':
            parking = True
        if _no_parking == 'on':
            parking = False

        image = image2 = image3 = image4 = image5 = image6 = image7 = image8 = image9 = None

        try:
            image = self.request.FILES['image']
        except :
            pass
        print('f', image)
        try:
            image2 = self.request.FILES['image2']
        except :
            pass
        try:
            image3 = self.request.FILES['image3']
        except :
            pass
        try:
            image4 = self.request.FILES['image4']
        except :
            pass
        try:
            image5 = self.request.FILES['image5']
        except :
            pass
        try:
            image6 = self.request.FILES['image6']
        except :
            pass
        try:
            image7 = self.request.FILES['image7']
        except :
            pass
        try:
            image8 = self.request.FILES['image8']
        except :
            pass
        try:
            image9 = self.request.FILES['image9']
        except :
            pass
        file_number= (self.request.POST['file_number'])
        pish = int(self.request.POST['pish'])
        pol_mhn = int(self.request.POST['pol_mhn'])
        bedroom = int(self.request.POST['bedroom'])
        area = int(self.request.POST['area'])
        description = self.request.POST['description']
        category = Category.objects.get(name='rhn-va-ejare')
        Product.objects.create(name=name, pish=pish, area=area,
            bedroom=bedroom, parking=parking, address=address,
            description=description, file_number=file_number,
            category=category, slug='ejare', type='ejare', image=image,
            image2 = image2, image3 = image3, image4 = image5, pol_mhn=pol_mhn,
            image6 = image6, image7 = image7, image8 = image8,  image9 = image9).save()
        return render(self.request, 'products/created.html', {})


class PrdouctCreateView(TemplateView):
    template_name = 'products/add_product.html'
    model = Product


class ProductListView(ListView):
    template_name='products/list.html'
    paginate_by = 4
    model = Product
    f = 0
    queryset = Product.objects.all()
    context_object_name = 'object_list'
    form_class = FilterProductForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        pish1_ = pish2_ = pol_mhn1_ = pol_mhn2_ = pol1_ = pol2_ = ''
        try:
            pish1_ = self.request.GET.get('pish1')
            pish2_ = self.request.GET.get('pish2')
            pol_mhn1_ = self.request.GET.get('pol_mhn1')
            pol_mhn2_ = self.request.GET.get('pol_mhn2')
        except:
            pass

        try:
            pol1_ = self.request.GET.get('pol1')
            pol2_ = self.request.GET.get('pol2')
        except:
            pass

        bedroom_ = self.request.GET.get('bedroom')
        met1_ = self.request.GET.get('met')
        met2_ =self.request.GET.get('met2')
        parking_ = self.request.GET.get('parking')
        no_parking_ = self.request.GET.get('no_parking')

        products = self.get_queryset()
        category = None
        categories = Category.objects.all()
        category_slug = self.kwargs.get('category_slug')

        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = self.queryset.filter(category=category)
        try:
            if pish1_ != None and pish2_ != '' and pish2_ != pish1_ and pish2_ != '0':
                if pish1_ == None :
                    pish1_ = 0
                products = products.filter(pish__gt=int(pish1_), pish__lt=int(pish2_)+1)
        except:
            pass

        try:
            if pol_mhn2_ != None and pol_mhn2_ != '' and pol_mhn2_ != pol_mhn1_ and pol_mhn2_ != '0':
                if pol_mhn1_ == None :
                    pol_mhn1_ = 0
                products = products.filter(pol_mhn__gt=int(pol_mhn1_), pol_mhn__lt=int(pol_mhn2_)+1)

        except:
            pass

        try:
            if not no_parking_ == parking_ and not no_parking_ == parking_ == None and not no_parking_ == parking_ == '':
                if parking_ == 'on':
                    products = products.filter(parking=True)
                if no_parking_ == 'on':
                    products = products.filter(parking=False)
        except:
            pass
        try:
            if  bedroom_ != None and bedroom_ != '':
                products = products.filter(bedroom=int(bedroom_))
        except:
            pass
        try:
            if pol2_ != None and pol2_ != '' and pol2_!=pol1_ and pol2_ != '0':
                if pol1_ == None :
                    pol1_ = 0
                products = products.filter(price__gt=int(pol1_), price__lt=int(pol2_)+1)
        except:
            pass
        try:
            if met2_ != None and met2_ != '' and met2_!=met1_ and met2_ != '0':
                if met1_ == None:
                    met1_ = 0
                products = products.filter(area__gt=int(met1_), area__lt=int(met2_)+1)
        except:
            pass

        self.object_list = products
        context = self.get_context_data()
        context['slug'] = category_slug
        return self.render_to_response(context)

    def get_queryset(self):
        return self.queryset

    def get_context_data(self, **kwargs):
        page = self.request.GET
        context = super().get_context_data(**kwargs)
        # print(context['urlp'])
        products =  context['object_list']
        context['form'] = FilterProductForm
        urlp = ''
        try:
            urlp = self.request.get_full_path().split('/products/?')[1]
            print('hi', urlp)

            try:
                if 'page=' in urlp:
                    if 'pol' in urlp:
                        print('hi2')
                        tmp = 'pol2='
                        urlp = urlp.split('&pol2=')[1]
                        urlp = tmp + urlp
                    else:
                        urlp = ''
            except :
                pass
        except:
            urlp = ''
        context['urlp'] = urlp
        context.update({'object_list':products})
        return context

class ProductDetailView(DetailView):
  
    template_name = 'products/detail2.html'
    queryset = Product.objects.all()
    context_object_name = 'object'
    # to override The url <int:pk> to <int:id>
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lst = Product.objects.all().order_by('-created')[:10]
        context.update({'lst': lst})
        return context
        
    def get_object(self):
        id_ = self.kwargs.get("id")
        slug_ = self.kwargs.get("slug")
        print('slug')
        return get_object_or_404(Product, id=id_, slug=slug_)

class ProductDeleteView(DetailView):
    template_name = 'products/delete.html'
    queryset = Product.objects.all()
    context_object_name = 'object'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_object(self):
        id_ = self.kwargs.get("id")
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Product, id=id_, slug=slug_)

    def post(self, request, *args, **kwargs):
        print('hi')
        id_ = self.kwargs.get("id")
        slug_ = self.kwargs.get("slug")
        Product.objects.get(id=id_, slug=slug_).delete()
        return render(self.request, 'products/deleted.html', {})

class ProductUpdateView(UpdateView):
    template_name = 'products/update.html'
    queryset = Product.objects.all()
    context_object_name = 'object'
    # to override The url <int:pk> to <int:id>
    def get_context_data(self, **kwargs):
        context ={}
        object = self.get_object()
        context['form'] = CompleteCreateForm(instance=object)
        return context


    def post(self, request, *args, **kwargs):
        id_ = self.kwargs.get("id")
        object = Product.objects.get(id=id_)
        name = self.request.POST['name']
        address = self.request.POST['address']
        parking = False
        _parking = None
        _no_parking = None
        try:
            _parking = self.request.POST['parking']
        except:
            pass
        try:
            _no_parking = self.request.POST['no_parking']
        except:
            pass
        
        if _parking == 'on':
            parking = True
        if _no_parking == 'on':
            parking = False

        image = image2 = image3 = image4 = image5 = image6 = image7 = image8 = image9 = None

        try:
            image = self.request.FILES['image']
        except :
            image = object.image
        print('f', image)
        try:
            image2 = self.request.FILES['image2']
        except :
            image2 = object.image2
        try:
            image3 = self.request.FILES['image3']
        except :
            image3 = object.image3
        try:
            image4 = self.request.FILES['image4']
        except :
            image4 = object.image4
        try:
            image5 = self.request.FILES['image5']
        except :
            image5 = object.image5
        try:
            image6 = self.request.FILES['image6']
        except :
            image6 = object.image6
        try:
            image7 = self.request.FILES['image7']
        except :
            image7 = object.image7
        try:
            image8 = self.request.FILES['image8']
        except :
            image8 = object.image8
        try:
            image9 = self.request.FILES['image9']
        except :
            image9 = object.image9
        
        nastaghi_ = False
        try:
            nastaghi = self.request.POST['nastaghi']
            if nastaghi == 'on':
                nastaghi_ = True
        except:
            pass
        
        file_number= (self.request.POST['file_number'])
        pish = int(self.request.POST['pish'])
        pol_mhn = int(self.request.POST['pol_mhn'])
        price_ = int(self.request.POST['price'])
        bedroom = int(self.request.POST['bedroom'])
        area = int(self.request.POST['area'])
        description = self.request.POST['description']
        category = Category.objects.get(name=object.category.name)
        Product.objects.create(name=name, pish=pish, area=area,
            bedroom=bedroom, parking=parking, price=price_, address=address,
            description=description, file_number=file_number,
            category=category, slug=object.slug, type=object.type, image=image,
            image2 = image2, image3 = image3, image4 = image5, pol_mhn=pol_mhn,
            image6 = image6, image7 = image7, image8 = image8,  image9 = image9, nastaghi=nastaghi_).save()
        Product.objects.get(id=object.id).delete()
        return render(self.request, 'products/created.html', {})

    def get_object(self):
        id_ = self.kwargs.get("id")
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Product, id=id_, slug=slug_)
