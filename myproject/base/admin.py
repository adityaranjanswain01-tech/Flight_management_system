from django.contrib import admin
from .models import *
# Register your models here.
class flightAdmin(admin.ModelAdmin):
    model= flightmodel
    list_display=['id','flight_company','flight_name','flight_number','flight_from','flight_to','flight_depaturetime','flight_date','flight_price']
    list_filter=['flight_company','flight_name']
    list_display_links=['id','flight_company','flight_name',]
    
class bookingAdmin(admin.ModelAdmin):
    model= Bookingmodel
    list_display=['id','flight_company','flight_name','flight_number','flight_from','flight_to','flight_depaturetime','flight_date','flight_price','pname','pemail','p_phone_no','p_Adhar_no','p_age','p_seat_class','seat_num']
    list_filter=['flight_company','flight_name','pname']
    list_display_links=['id','flight_company','flight_name',]
    
class historyAdmin(admin.ModelAdmin):
    model= historymodel
    list_display=['id','flight_company','flight_name','flight_number','flight_from','flight_to','flight_depaturetime','flight_date','flight_price','pname','pemail','p_phone_no','p_Adhar_no','p_age','p_seat_class','seat_num']
    list_filter=['flight_company','flight_name','pname']
    list_display_links=['id','flight_company','flight_name',]      
    
admin.site.register(flightmodel,flightAdmin)
admin.site.register(Bookingmodel,bookingAdmin)
admin.site.register(historymodel,historyAdmin)

