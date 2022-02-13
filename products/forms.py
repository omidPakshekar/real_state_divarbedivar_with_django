from django import forms
from .models import Product
from django.db import models

class EjareCreateForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(EjareCreateForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Product
        fields = ['address', 'description', 'name', 'bedroom', 'year',
            'file_number', 'image', 'image2', 'image3', 'image4',
            'image5', 'image6', 'image7', 'image8', 'image9', 'pish', 'pol_mhn']

    year = forms.IntegerField(
        widget=forms.NumberInput(
            attrs = {
                "style" : "width: 20%; height:10%;",
                " class": "qty-text",
                "id": "qty"
            }
        ) ,required=False, initial=0
    )
    address = forms.CharField(widget=forms.Textarea(
        attrs = {
            "style" : "width: 70%; height: 100px;"
        }
    ), required=True)
    description = forms.CharField(widget=forms.Textarea(
        attrs = {
            "style" : "width: 600px; height: 200px;"
        }
    ),initial=' ', required=True)
    name = forms.CharField(widget=forms.TextInput(
        attrs = {
            "style" : "width: 50%;"
        }
    ),required=True)
    bedroom = forms.IntegerField(
        widget=forms.NumberInput(
            attrs = {
                "style" : "width: 20%; height:10%;",
                " class": "qty-text",
                "id": "qty"
            }
        ) ,required=False, initial=0
    )

    file_number = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                "style" : "width: 20%; height:10%;",
                " class": "qty-text",
                "id": "qty"
            }
        ) ,required=False, initial=0
    )
    area = forms.IntegerField(
        widget=forms.NumberInput(
            attrs = {
                "style" : "width: 20%; height:10%;",
                " class": "qty-text",
                "id": "qty"
            }
        ) ,required=False, initial=0
    )
    pish = forms.IntegerField(widget=forms.NumberInput(
        attrs = {
            "style" : "width: 25%;"
        }
    ),initial=0, required=True)
    pol_mhn = forms.IntegerField(widget=forms.NumberInput(
        attrs = {
            "style" : "width: 25%;"
        }
    ),initial=0, required=True)

    parking = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs = {
                "style" : "width:17px; height:17px;"
            }
    )
        ,required=False,
        initial=False)

    no_parking = forms.BooleanField(
        required=False,
        widget = forms.CheckboxInput(
        attrs = {
            "style" : "width:17px; height:17px;"
        }),
        initial=False
    )
    image = forms.ImageField(required=False)
    image2 = forms.ImageField(required=False)
    image3 = forms.ImageField(required=False)
    image4 = forms.ImageField(required=False)
    image5 = forms.ImageField(required=False)
    image6 = forms.ImageField(required=False)
    image7 = forms.ImageField(required=False)
    image8 = forms.ImageField(required=False)
    image9 = forms.ImageField(required=False)

    def clean(self):
        try:
            self.cleaned_data['year'] = int(self.cleaned_data['year'])
        except:
            self.cleaned_data['year'] = 0
        try:
            self.cleaned_data['pol_mhn'] = int(self.cleaned_data['pol_mhn'])
        except :
            self.cleaned_data['pol_mhn'] = 0
        try :
            self.cleaned_data['pish'] = int(self.cleaned_data['pish'])
        except :
            self.cleaned_data['pish'] = 0

        try:
            self.cleaned_data['price'] = int(self.cleaned_data['price'])
        except :
            self.cleaned_data['price'] = 0

        try :
            self.cleaned_data['price_met'] = int(self.cleaned_data['price_met'])
        except :
            self.cleaned_data['price_met'] = 0

        try:
            self.cleaned_data['area'] = int(self.cleaned_data['area'])
        except :
            self.cleaned_data['area'] = 0
        try:
            self.cleaned_data['bedroom'] = int(self.cleaned_data['bedroom'])
        except:
            self.cleaned_data['bedroom'] = 0

class RhnCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(RhnCreateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Product
        fields = ['address', 'description', 'name', 'bedroom', 'year',
                    'file_number', 'pish', 'image', 'image2', 'image3', 'image4',
                     'image5', 'image6', 'image7', 'image8', 'image9']



    address = forms.CharField(widget=forms.Textarea(
        attrs = {
            "style" : "width: 70%; height: 100px;"
        }
    ), required=True)
    description = forms.CharField(widget=forms.Textarea(
        attrs = {
            "style" : "width: 70%; height: 200px;"
        }
    ),initial=' ', required=True)
    name = forms.CharField(widget=forms.TextInput(
        attrs = {
            "style" : "width: 50%;"
        }
    ),required=True)
    bedroom = forms.IntegerField(
        widget=forms.NumberInput(
            attrs = {
                "style" : "width: 20%; height:10%;",
                " class": "qty-text",
                "id": "qty"
            }
        ) ,required=False, initial=0
    )
    year = forms.IntegerField(
        widget=forms.NumberInput(
            attrs = {
                "style" : "width: 20%; height:10%;",
                " class": "qty-text",
                "id": "qty"
            }
        ) ,required=False, initial=0
    )
    file_number = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                "style" : "width: 20%; height:10%;",
                " class": "qty-text",
                "id": "qty"
            }
        ) ,required=False, initial=0
    )
    area = forms.IntegerField(
        widget=forms.NumberInput(
            attrs = {
                "style" : "width: 20%; height:10%;",
                " class": "qty-text",
                "id": "qty"
            }
        ) ,required=False, initial=0
    )
    pish = forms.IntegerField(widget=forms.NumberInput(
        attrs = {
            "style" : "width: 25%;"
        }
    ),initial=0, required=True)

    parking = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs = {
                "style" : "width:17px; height:17px;"
            }
    )
        ,required=False,
        initial=False)

    no_parking = forms.BooleanField(
        required=False,
        widget = forms.CheckboxInput(
        attrs = {
            "style" : "width:17px; height:17px;"
        }),
        initial=False
    )


    image = forms.ImageField(required=False)
    image2 = forms.ImageField(required=False)
    image3 = forms.ImageField(required=False)
    image4 = forms.ImageField(required=False)
    image5 = forms.ImageField(required=False)
    image6 = forms.ImageField(required=False)
    image7 = forms.ImageField(required=False)
    image8 = forms.ImageField(required=False)
    image9 = forms.ImageField(required=False)

    def validate(self, value):
        """Check if value consists only of valid emails."""
        # Use the parent's handling of required fields, etc.
        print('amir', super().validate(value))

    def clean(self):
        try:
            self.cleaned_data['year'] = int(self.cleaned_data['year'])
        except:
            self.cleaned_data['year'] = 0
        try:
            self.cleaned_data['pol_mhn'] = int(self.cleaned_data['pol_mhn'])
        except :
            self.cleaned_data['pol_mhn'] = 0
        try :
            self.cleaned_data['pish'] = int(self.cleaned_data['pish'])
        except :
            self.cleaned_data['pish'] = 0

        try:
            self.cleaned_data['price'] = int(self.cleaned_data['price'])
        except :
            self.cleaned_data['price'] = 0

        try :
            self.cleaned_data['price_met'] = int(self.cleaned_data['price_met'])
        except :
            self.cleaned_data['price_met'] = 0

        try :
            self.cleaned_data['area'] = int(self.cleaned_data['area'])
        except :
            self.cleaned_data['area'] = 0
        try:
            self.cleaned_data['bedroom'] = int(self.cleaned_data['bedroom'])
        except:
            self.cleaned_data['bedroom'] = 0

        _no_parking = self.cleaned_data['no_parking']
        _parking = self.cleaned_data['parking']
        self.cleaned_data['parking'] = True if _parking == True or (_parking == False and _no_parking ) else  False;
        del self.cleaned_data['no_parking']






class FroshCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(FroshCreateForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Product
        fields = ['address', 'description', 'name', 'bedroom', 'year', 'price_met',
            'file_number', 'price', 'image', 'image2', 'image3', 'image4',
             'image5', 'image6', 'image7', 'image8', 'image9']

    address = forms.CharField(widget=forms.Textarea(
        attrs = {
            "style" : "width: 70%; height: 100px;"
        }
    ), required=True)
    description = forms.CharField(widget=forms.Textarea(
        attrs = {
            "style" : "width: 600px; height: 200px;"
        }
    ),initial=' ', required=False)
    name = forms.CharField(widget=forms.TextInput(
        attrs = {
            "style" : "width: 50%;"
        }
    ),required=True)
    bedroom = forms.IntegerField(
        widget=forms.NumberInput(
            attrs = {
                "style" : "width: 20%; height:10%;",
                " class": "qty-text",
                "id": "qty"
            }
        ) ,required=False, initial=0
    )
    year = forms.IntegerField(
        widget=forms.NumberInput(
            attrs = {
                "style" : "width: 20%; height:10%;",
                " class": "qty-text",
                "id": "qty"
            }
        ) ,required=False, initial=0
    )
    file_number = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                "style" : "width: 20%; height:10%;",
                " class": "qty-text",
                "id": "qty"
            }
        ) ,required=False, initial=0
    )
    area = forms.IntegerField(
        widget=forms.NumberInput(
            attrs = {
                "style" : "width: 20%; height:10%;",
                " class": "qty-text",
                "id": "qty"
            }
        ) ,required=False, initial=0
    )
    price = forms.IntegerField(widget=forms.NumberInput(
        attrs = {
            "style" : "width: 25%;"
        }
    ),initial=0, required=False)


    price_met = forms.IntegerField(widget=forms.NumberInput(
        attrs = {
            "style" : "width: 25%;"
        }
    ), initial=0, required=False)

    pish = forms.IntegerField(widget=forms.NumberInput(
        attrs = {
            "style" : "width: 25%;"
        }
    ), initial=0, required=False)

    parking = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs = {
                "style" : "width:17px; height:17px;"
            }
    )
    ,required=False,
    initial=False)

    no_parking = forms.BooleanField(
    required=False,
    widget = forms.CheckboxInput(
        attrs = {
            "style" : "width:17px; height:17px;"
        }),
    initial=False)

    nastaghi = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs = {
                "style" : "width:17px; height:17px;"
            }
    )
    ,required=False,
    initial=False)

    no_nastaghi = forms.BooleanField(
        required=False,
        widget = forms.CheckboxInput(
            attrs = {
                "style" : "width:17px; height:17px;"
            }),
        initial=False)

    def clean(self):

        try:
            self.cleaned_data['year'] = int(self.cleaned_data['year'])
        except:
            self.cleaned_data['year'] = 0
        try:
            self.cleaned_data['pol_mhn'] = int(self.cleaned_data['pol_mhn'])
        except :
            self.cleaned_data['pol_mhn'] = 0
        try :
            self.cleaned_data['pish'] = int(self.cleaned_data['pish'])
        except :
            self.cleaned_data['pish'] = 0

        try :
            self.cleaned_data['price'] = int(self.cleaned_data['price'])
        except :
            self.cleaned_data['price'] = 0

        try :
            self.cleaned_data['price_met'] = int(self.cleaned_data['price_met'])
        except :
            self.cleaned_data['price_met'] = 0

        try :
            self.cleaned_data['area'] = int(self.cleaned_data['area'])
        except :
            self.cleaned_data['area'] = 0
        try:
            self.cleaned_data['bedroom'] = int(self.cleaned_data['bedroom'])
        except:
            self.cleaned_data['bedroom'] = 0


        _no_parking = self.cleaned_data['no_parking']
        _parking = self.cleaned_data['parking']
        self.cleaned_data['parking'] = True if _parking == True or (_parking == False and _no_parking ) else  False;
        _no_nastaghi = self.cleaned_data['no_nastaghi']
        _nastaghi = self.cleaned_data['nastaghi']
        self.cleaned_data['nastaghi'] = True if _nastaghi == True or (_nastaghi == False and _no_nastaghi ) else  False;


        del self.cleaned_data['no_parking']
        del self.cleaned_data['no_nastaghi']


class CompleteCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(CompleteCreateForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Product
        fields = '__all__'


    address = forms.CharField(widget=forms.Textarea(
        attrs = {
            "style" : "width: 70%; height: 100px;"
        }
    ), required=True)
    description = forms.CharField(widget=forms.Textarea(
        attrs = {
            "style" : "width: 600px; height: 200px;"
        }
    ),initial=' ', required=False)
    name = forms.CharField(widget=forms.TextInput(
        attrs = {
            "style" : "width: 50%;"
        }
    ),required=True)
    bedroom = forms.IntegerField(
        widget=forms.NumberInput(
            attrs = {
                "style" : "width: 20%; height:10%;",
                " class": "qty-text",
                "id": "qty"
            }
        ) ,required=False, initial=0
    )
    year = forms.IntegerField(
        widget=forms.NumberInput(
            attrs = {
                "style" : "width: 20%; height:10%;",
                " class": "qty-text",
                "id": "qty"
            }
        ) ,required=False, initial=0
    )
    file_number = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                "style" : "width: 20%; height:10%;",
                " class": "qty-text",
                "id": "qty"
            }
        ) ,required=False, initial=0
    )
    area = forms.IntegerField(
        widget=forms.NumberInput(
            attrs = {
                "style" : "width: 20%; height:10%;",
                " class": "qty-text",
                "id": "qty"
            }
        ) ,required=False, initial=0
    )
    price = forms.IntegerField(widget=forms.NumberInput(
        attrs = {
            "style" : "width: 25%;"
        }
    ),initial=0, required=False)


    price_met = forms.IntegerField(widget=forms.NumberInput(
        attrs = {
            "style" : "width: 25%;"
        }
    ), initial=0, required=False)

    pish = forms.IntegerField(widget=forms.NumberInput(
        attrs = {
            "style" : "width: 25%;"
        }
    ), initial=0, required=False)

    pol_mhn = forms.IntegerField(widget=forms.NumberInput(
        attrs = {
            "style" : "width: 25%;"
        }
    ), initial=0, required=False)


    parking = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs = {
                "style" : "width:17px; height:17px;"
            }
    )
    ,required=False,
    initial=False)

    no_parking = forms.BooleanField(
    required=False,
    widget = forms.CheckboxInput(
        attrs = {
            "style" : "width:17px; height:17px;"
        }),
    initial=False)

    nastaghi = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs = {
                "style" : "width:17px; height:17px;"
            }
    )
    ,required=False,
    initial=False)

    no_nastaghi = forms.BooleanField(
        required=False,
        widget = forms.CheckboxInput(
            attrs = {
                "style" : "width:17px; height:17px;"
            }),
        initial=False)
    year = forms.IntegerField(
        widget=forms.NumberInput(
            attrs = {
                "style" : "width: 20%; height:10%;",
                " class": "qty-text",
                "id": "qty"
            }
        ) ,required=False, initial=0
    )

    image = forms.ImageField(required=False)
    image2 = forms.ImageField(required=False)
    image3 = forms.ImageField(required=False)
    image4 = forms.ImageField(required=False)
    image5 = forms.ImageField(required=False)
    image6 = forms.ImageField(required=False)
    image7 = forms.ImageField(required=False)
    image8 = forms.ImageField(required=False)
    image9 = forms.ImageField(required=False)

    def clean(self):
        try:
            self.cleaned_data['year'] = int(self.cleaned_data['year'])
        except:
            self.cleaned_data['year'] = 0
        try:
            self.cleaned_data['pol_mhn'] = int(self.cleaned_data['pol_mhn'])
        except :
            self.cleaned_data['pol_mhn'] = 0
        try :
            self.cleaned_data['pish'] = int(self.cleaned_data['pish'])
        except :
            self.cleaned_data['pish'] = 0

        try :
            self.cleaned_data['price'] = int(self.cleaned_data['price'])
        except :
            self.cleaned_data['price'] = 0

        try:
            self.cleaned_data['price_met'] = int(self.cleaned_data['price_met'])
        except :
            self.cleaned_data['price_met'] = 0

        try :
            self.cleaned_data['area'] = int(self.cleaned_data['area'])
        except :
            self.cleaned_data['area'] = 0
        try:
            self.cleaned_data['bedroom'] = int(self.cleaned_data['bedroom'])
        except:
            self.cleaned_data['bedroom'] = 0


        _no_parking = self.cleaned_data['no_parking']
        _parking = self.cleaned_data['parking']
        self.cleaned_data['parking'] = True if _parking == True or (_parking == False and _no_parking ) else  False;
        _no_nastaghi = self.cleaned_data['no_nastaghi']
        _nastaghi = self.cleaned_data['nastaghi']
        self.cleaned_data['nastaghi'] = True if _nastaghi == True or (_nastaghi == False and _no_nastaghi ) else  False;
        del self.cleaned_data['no_parking']
        del self.cleaned_data['no_nastaghi']


class FilterProductForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(FilterProductForm, self).__init__(*args, **kwargs)
    # we use coerce=int to convert the input to the int
    btn_click = forms.BooleanField(
        widget=forms.HiddenInput()
    )
    bedroom = forms.IntegerField(
        widget=forms.NumberInput(
            attrs = {
                "style" : "width: 20%; height:10%;",
                " class": "qty-text",
                "id": "qty"
            }
        ) ,required=False
    )
    bedroom2 = forms.IntegerField(
        widget=forms.NumberInput(
            attrs = {
                "style" : "width: 10%;",
                " class": "qty-text",
                "id": "qty2"
            }
        ) ,required=False
    )
    pol1 = forms.IntegerField(widget=forms.NumberInput(
        attrs = {
            "style" : "width: 95%;"
        }
    ),initial=0, required=False)
    pol2 = forms.IntegerField(widget=forms.NumberInput(
        attrs = {
            "style" : "width: 95%;"
        }
    ),initial=0, required=False)


    met1 = forms.IntegerField(widget=forms.NumberInput(
        attrs = {
            "style" : "width: 95%;"
        }
    ), initial=0, required=False)
    met2 = forms.IntegerField(widget=forms.NumberInput(
        attrs = {
            "style" : "width: 95%;"
        }
    ), initial=0, required=False)

    pish1 = forms.IntegerField(widget=forms.NumberInput(
        attrs = {
            "style" : "width: 95%;"
        }
    ),initial=0, required=False)
    pish2 = forms.IntegerField(widget=forms.NumberInput(
        attrs = {
            "style" : "width: 95%;"
        }
    ),initial=0, required=False)

    pol_mhn1 = forms.IntegerField(widget=forms.NumberInput(
        attrs = {
            "style" : "width: 95%;"
        }
    ),initial=0, required=False)
    pol_mhn2 = forms.IntegerField(widget=forms.NumberInput(
        attrs = {
            "style" : "width: 95%;"
        }
    ),initial=0, required=False)


    parking = forms.BooleanField(
        widget = forms.CheckboxInput(
            attrs = {
                "style" : "width:17px; height:17px;"
            }
        )
        ,required=False,
        initial=False)

    no_parking = forms.BooleanField(
    required=False,
    widget = forms.CheckboxInput(
        attrs = {
            "style" : "width:17px; height:17px;"
        }),
    initial=False)
