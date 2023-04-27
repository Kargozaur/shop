from django.contrib import admin
from .models import category, user, order, order_items, product, delievery
# Register your models here.

admin.site.register(category)
admin.site.register(user)
admin.site.register(order)
admin.site.register(order_items)
admin.site.register(product)
admin.site.register(delievery)