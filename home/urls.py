from django.urls import path, include
from . import views
app_name='home'

urlpatterns = [
    # main page
    path('',  views.MainPageView.as_view() ,name='main-page'),
]
