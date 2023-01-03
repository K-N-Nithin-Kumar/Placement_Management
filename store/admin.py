'''from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)'''

from django.contrib import admin
from .models.product import Company
from .models.category import Category
from .models.customer import Student
from .models.orders import Application


class AdminCompany(admin.ModelAdmin):
    list_display = ['name', 'cgpa', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.register(Company, AdminCompany)
admin.site.register(Category, AdminCategory)
admin.site.register(Student)
admin.site.register(Application)
