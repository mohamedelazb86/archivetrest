from django.urls import path
from . import views

app_name='contractor'

urlpatterns = [
    path('',views.contractor,name='contractor'),
    path('add-contractor',views.add_contractor,name='add-contractor'),
]
