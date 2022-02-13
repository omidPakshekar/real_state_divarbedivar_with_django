from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.views import View
from django.http import HttpResponse
from .forms import FilterProductForm, FroshCreateForm, RhnCreateForm, EjareCreateForm

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
        file_number= int(self.request.POST['file_number'])
        price_met = int(self.request.POST['price_met'])
        price = int(self.request.POST['price'])
        bedroom = int(self.request.POST['bedroom'])
        year = int(self.request.POST['year'])
        area = int(self.request.POST['area'])
        description = self.request.POST['description']
        category = Category.objects.get(name='فروش')
        Product.objects.create(name=name, price_met=price_met, price=price, area=area, year=year,
            bedroom=bedroom, parking=parking, address=address,
            description=description, file_number=file_number,
            category=category, slug='frosh', type='frosh', image=image,
            image2 = image2, image3 = image3, image4 = image5,
            image6 = image6, image7 = image7, image8 = image8,  image9 = image9).save()
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
        file_number= int(self.request.POST['file_number'])
        price_met = int(self.request.POST['price_met'])
        price = int(self.request.POST['price'])
        bedroom = int(self.request.POST['bedroom'])
        year = int(self.request.POST['year'])
        area = int(self.request.POST['area'])
        description = self.request.POST['description']
        category = Category.objects.get(name='ویلا')
        Product.objects.create(name=name, price_met=price_met, price=price, area=area, year=year,
            bedroom=bedroom, parking=parking, address=address,
            description=description, file_number=file_number,
            category=category, slug='villa', type='villa', image=image,
            image2 = image2, image3 = image3, image4 = image5,
            image6 = image6, image7 = image7, image8 = image8,  image9 = image9).save()
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
            image8 = self.request.FILES['impriceage8']
        except :
            pass
        try:
            image9 = self.request.FILES['image9']
        except :
            pass
        file_number= int(self.request.POST['file_number'])
        price_met = int(self.request.POST['price_met'])
        price = int(self.request.POST['price'])
        bedroom = int(self.request.POST['bedroom'])
        year = int(self.request.POST['year'])
        area = int(self.request.POST['area'])
        description = self.request.POST['description']
        category = Category.objects.get(name='پروژه')
        Product.objects.create(name=name, price_met=price_met, price=price, area=area, year=year,
            bedroom=bedroom, parking=True, address=address,
            description=description, file_number=file_number,
            category=category, slug='proje', type='proje', image=image,
            image2 = image2, image3 = image3, image4 = image5,
            image6 = image6, image7 = image7, image8 = image8,  image9 = image9).save()
        return render(self.request, 'products/created.html', {})
# ********************* rhn ****************************
class RhnCreateView(CreateView):
    template_name = 'products/add_rhn.html'
    model = Product
    form_class = RhnCreateForm
    # redirect = 'orders:order-created'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'form':RhnCreateForm})
        return context
    def get(self, request, *args, **kwargs):
        return render(self.request, 'products/add_rhn.html', {'form':RhnCreateForm})

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
        file_number= int(self.request.POST['file_number'])
        pish = int(self.request.POST['pish'])
        bedroom = int(self.request.POST['bedroom'])
        area = int(self.request.POST['area'])
        description = self.request.POST['description']
        category = Category.objects.get(name='رهن و اجاره')
        Product.objects.create(name= name,pish=pish, area=area,
            bedroom=bedroom, parking=parking, address=address,
            description=description, file_number=file_number,
            category=category, slug='rhn', type='rhn', image=image,
            image2 = image2, image3 = image3, image4 = image5,
            image6 = image6, image7 = image7, image8 = image8,  image9 = image9).save()
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
        file_number= int(self.request.POST['file_number'])
        pish = int(self.request.POST['pish'])
        pol_mhn = int(self.request.POST['pol_mhn'])
        bedroom = int(self.request.POST['bedroom'])
        area = int(self.request.POST['area'])
        description = self.request.POST['description']
        category = Category.objects.get(name='رهن و اجاره')
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
        print('fff')
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
    # for default look in appname/modelname_list.html for templates
    # or you can change templates directory with
    template_name = 'products/detail2.html'
    queryset = Product.objects.all()
    context_object_name = 'object'
    # to override The url <int:pk> to <int:id>
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lst = Product.objects.all().order_by('-created')[:10]
        context.update({'lst': lst})
        return context
    def post(self, request, *args, **kwargs):
        id_ = self.kwargs.get("id")
        Product.objects.get(id=id_).delete()
        return render(self.request, 'products/deleted.html', {})

    def get_object(self):
        id_ = self.kwargs.get("id")
        slug_ = self.kwargs.get("slug")
        print('slug')
        return get_object_or_404(Product, id=id_, slug=slug_)
