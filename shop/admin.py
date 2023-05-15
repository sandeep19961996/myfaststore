from pyexpat import model
from django.utils.html import format_html
from django.urls import reverse
from django.contrib import admin
from .models import Customer,Product,Cart,OrderPlaced
from django.utils.safestring import mark_safe
# Register your models here.

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name','locality','city', 'zipcode','state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','product_slug', 'title', 'selling_price','discounted_price','description', 'brand','category','admin_photo']
    # fields=['admin_photo']

    # readonly_fields=('admin_photo',)

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product','quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'user', 'customer','customer_info','product','product_info','image_info','quantity', 'ordered_date','status']

 def customer_info(self,obj): 
   link =  reverse("admin:shop_customer_change", args=[obj.customer.pk])
   return format_html('<a href="{}">{}</a>',link, obj.customer.name)
 
 def product_info(self,obj): 
   link =  reverse("admin:shop_product_change", args=[obj.product.pk])
   return format_html('<a href="{}">{}</a>',link, obj.product.title)
 
 def image_info(self,obj): 
    link =  reverse("admin:shop_product_change", args=[obj.product.pk])
    return format_html('<img src="{}" width="100" />',link, obj.product.product_image)
 

   