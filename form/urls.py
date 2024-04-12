from django.urls import path
from form import views

urlpatterns = [
    path('', views.afficher_form, name='HtmlForm'),
    path('gerer_HtmlForm/', views.form, name='form'),

]