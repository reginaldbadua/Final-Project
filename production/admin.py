from django.contrib import admin
from .models import Detail, Product, Demand_Signal

class DetailAdmin(admin.ModelAdmin): 
    list_display = ('id', 'abv')

# Register your models here.
class Demand_SignalAdmin (admin.ModelAdmin):
    list_display = ('demand_score', 'detail_id')

admin.site.register(Detail, DetailAdmin)
admin.site.register(Product)
admin.site.register(Demand_Signal)