from django.contrib import admin
from .models import Category, Subcategory, Item , Order , OrderItem

class OrderInline(admin.TabularInline):
    model=OrderItem
class OrderAdmin(admin.ModelAdmin):
    inlines=(OrderInline,)


admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Item)
admin.site.register(Order,OrderAdmin)
