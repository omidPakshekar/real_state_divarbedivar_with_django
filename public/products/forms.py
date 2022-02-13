from django import forms
from .models import Product
from django.db import models

class EjareCreateForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(EjareCreateForm, self).__init__(*args, **kwargs)

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

    file_number = forms.IntegerField(
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
    pish = forms.IntegerField(widget=forms.TextInput(
        attrs = {
            "style" : "width: 25%;"
        }
    ),initial=0, required=True)
    pol_mhn = forms.IntegerField(widget=forms.TextInput(
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

class RhnCreateForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(RhnCreateForm, self).__init__(*args, **kwargs)

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

    file_number = forms.IntegerField(
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
    pish = forms.IntegerField(widget=forms.TextInput(
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


class FroshCreateForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(FroshCreateForm, self).__init__(*args, **kwargs)

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
    file_number = forms.IntegerField(
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
    price = forms.IntegerField(widget=forms.TextInput(
        attrs = {
            "style" : "width: 25%;"
        }
    ),initial=0, required=True)


    price_met = forms.IntegerField(widget=forms.TextInput(
        attrs = {
            "style" : "width: 25%;"
        }
    ), initial=0, required=True)
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
    image = forms.ImageField(required=False)
    image2 = forms.ImageField(required=False)
    image3 = forms.ImageField(required=False)
    image4 = forms.ImageField(required=False)
    image5 = forms.ImageField(required=False)
    image6 = forms.ImageField(required=False)
    image7 = forms.ImageField(required=False)
    image8 = forms.ImageField(required=False)
    image9 = forms.ImageField(required=False)

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
    pol1 = forms.IntegerField(widget=forms.TextInput(
        attrs = {
            "style" : "width: 95%;"
        }
    ),initial=0, required=False)
    pol2 = forms.IntegerField(widget=forms.TextInput(
        attrs = {
            "style" : "width: 95%;"
        }
    ),initial=0, required=False)


    met1 = forms.IntegerField(widget=forms.TextInput(
        attrs = {
            "style" : "width: 95%;"
        }
    ), initial=0, required=False)
    met2 = forms.IntegerField(widget=forms.TextInput(
        attrs = {
            "style" : "width: 95%;"
        }
    ), initial=0, required=False)

    pish1 = forms.IntegerField(widget=forms.TextInput(
        attrs = {
            "style" : "width: 95%;"
        }
    ),initial=0, required=False)
    pish2 = forms.IntegerField(widget=forms.TextInput(
        attrs = {
            "style" : "width: 95%;"
        }
    ),initial=0, required=False)

    pol_mhn1 = forms.IntegerField(widget=forms.TextInput(
        attrs = {
            "style" : "width: 95%;"
        }
    ),initial=0, required=False)
    pol_mhn2 = forms.IntegerField(widget=forms.TextInput(
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
