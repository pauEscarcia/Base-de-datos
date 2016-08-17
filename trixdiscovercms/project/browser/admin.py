from django.contrib import admin
from .models import Country,State,City,Images,Category,Classification,Activity,Provider
 #Category, Clasification, Activity, Provider,Country,Entity,Municipality 

# Register your models here.
admin.site.register(Category)
admin.site.register(Classification)
admin.site.register(Activity)
admin.site.register(Provider)

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)

admin.site.register(Images)
