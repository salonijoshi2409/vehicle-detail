from django.contrib import admin

# Register your models here.
from .models import Vechicle
# Register your models here.
@admin.register(Vechicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display=['name' , 'speed', 'avgspeed', 'fuellev', 'enginestat', 'temp', 'on_off']