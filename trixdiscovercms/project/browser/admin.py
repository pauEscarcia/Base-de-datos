from django.contrib import admin
from .models import  Category, Clasification, Activity, Provider,Country,Entity,Municipality 

# Register your models here.
admin.site.register(Category)
admin.site.register(Clasification)
admin.site.register(Activity)
admin.site.register(Provider)

admin.site.register(Country)
admin.site.register(Entity)
admin.site.register(Municipality)