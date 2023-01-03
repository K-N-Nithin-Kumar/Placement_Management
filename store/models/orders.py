from django.db import models
from .product import Company
from .customer import Student
import datetime


class Application(models.Model):
    product = models.ForeignKey(Company,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Student,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cgpa= models.IntegerField()
    profile = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Application.objects.filter(customer=customer_id).order_by('-date')