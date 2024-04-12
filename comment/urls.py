from django.urls import path
from comment import views

urlpatterns = [
  
    path('enregistrer_commentaire/', views.submit_comment, name='enregistrer_commentaire'),

]