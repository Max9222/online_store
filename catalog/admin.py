from django.contrib import admin

from catalog.models import Product, Category, Blog, Possibilities


#admin.site.register(Product)
#admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'purchase_price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

# @admin.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('title ',)
admin.site.register(Blog)

@admin.register(Possibilities)
class PossibilitiesAdmin(admin.ModelAdmin):
    list_display = ('title', 'product',)
    list_filter = ('product',)
