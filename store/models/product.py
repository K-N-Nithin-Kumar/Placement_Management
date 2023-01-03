# from django.db import models
# from .category import Category
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=30)
#     price = models.IntegerField(default=0)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
#     description = models.CharField(max_length=200, default="", null=True, blank=True)
#     image = models.ImageField(upload_to='uploads/products/')
#
#     @staticmethod
#     def get_all_products():
#         return Product.objects.all()
#
#     @staticmethod
#     def get_all_products_bycategoryid(category_id):
#         if category_id:
#             return Product.objects.filter(category=category_id)
#         else:
#             return Product.get_all_products()


from django.db import models
from .category import Category


class Company(models.Model):
    name = models.CharField(max_length=50)
    cgpa= models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_products_by_id(ids):
        return Company.objects.filter(id__in =ids)

    @staticmethod
    def get_all_products():
        return Company.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Company.objects.filter(category = category_id)
        else:
            return Company.get_all_products();