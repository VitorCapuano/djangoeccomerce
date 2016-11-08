from django.contrib import admin

# Register your models here.
from catalog.models import Product,Category



class CategoryAdmin(admin.ModelAdmin):
    #Lista de campos exibidos na listagem
    list_display = ['name', 'slug','created','modified']
    #Search Fields quais campos pode pesquisar
    search_fields = ['name','slug']
    #Listagem lateral
    list_filter = ['created','modified']


class ProductAdmin(admin.ModelAdmin):
    #Lista de campos exibidos na listagem
    list_display = ['name', 'slug','category','created','modified']
    #Search Fields quais campos pode pesquisar, lookups pesquisar produtos com essa categoria
    search_fields = ['name','slug', 'category__name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)