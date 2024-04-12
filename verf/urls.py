from django.urls import path
from verf import views

urlpatterns = [
    path('reservation/', views.reservation, name='reservation'),

   

]