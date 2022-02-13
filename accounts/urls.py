from django.urls import path, include
from . import views
app_name='accounts'

urlpatterns = [
    path('login/',  views.CustomLoginView.as_view() ,name='login'),
    path('logout/',  views.CustomLogOutView.as_view() ,name='logout')
]
