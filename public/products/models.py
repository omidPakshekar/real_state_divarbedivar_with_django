from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True)

    class Meta:
        # if we use - befor name --> -name “-” prefix, which indicates descending order.
        ordering = ('name',)
        # verbose_name is A human-readable name for the object, singular:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:list-product-category', kwargs={'category_slug': self.slug})


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)

    CHOICES = [
        ('frosh', 'frosh'),
        ('villa', 'villa'),
        ('rhn', 'rhn'),
        ('ejare', 'ejare'),
        ('proje', 'proje'),
    ]
    type = models.CharField(
        max_length=5,
        choices = CHOICES,
        default='frosh',
    )

    file_number = models.PositiveIntegerField(default=1)
    # image
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image2 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image3 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image4 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image5 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image6 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image7 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image8 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image9 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image10 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image11 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image12 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image13 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image14 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image15 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image16 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image17 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image18 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image19 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    image20 = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)

    # dste bndi
    price_met = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    pol_mhn = models.PositiveIntegerField(default=0)
    pish =  models.PositiveIntegerField(default=0)

    bedroom = models.PositiveIntegerField(default=0)
    area = models.PositiveIntegerField(default=0)
    year = models.PositiveIntegerField(default=1)
    parking = models.BooleanField(default=False)
    map = models.TextField(default="", blank=True)
    address = models.TextField()
    description = models.TextField(blank=True)
    # age rhn va ejare bshe

    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ('-created',)
        # we difine this becaue we plane to query products by both
        # id and slug together to improve performance for querys to utlis
        # two field
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product-detail', kwargs={'id': self.id, 'slug':self.slug})
