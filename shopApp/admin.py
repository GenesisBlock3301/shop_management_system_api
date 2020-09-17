from django.contrib import admin
from .models import *
admin.site.register(User)
# admin.site.register(Employee)
# admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Rating)
admin.site.register(Transaction)
admin.site.register(Comment)
admin.site.register(Cart)
admin.site.register(CartItem)