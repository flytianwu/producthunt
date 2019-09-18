from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'hunter', 'votes_total', 'pub_date')
    exclude = ('pub_date',)


admin.site.register(Product, ProductAdmin)
