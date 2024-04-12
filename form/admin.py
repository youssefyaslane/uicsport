from django.contrib import admin
from .models import Inscription

@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):

    list_display = ('full_name', 'email', 'number')


admin.site.unregister(Inscription)  
admin.site.register(Inscription, InscriptionAdmin)
    
