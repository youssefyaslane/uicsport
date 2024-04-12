from django.contrib import admin
from .models import Terrain, Reservation
from django.contrib.auth.models import User 

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('terrain', 'date_heure_debut', 'date_heure_fin')

@admin.register(Terrain)
class TerrainAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(Reservation)
admin.site.unregister(Terrain)    
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Terrain, TerrainAdmin)