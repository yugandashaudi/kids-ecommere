
from django.db import models
from django.contrib.auth.models import User
from numpy import require 
from phonenumber_field.modelfields import PhoneNumberField

class ProfileVendor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,blank=False)
    middle_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,blank=False)
    address = models.CharField(max_length=100,blank=False)
    email = models.CharField(max_length=100,blank=False)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)


product_size =[
    ('XL','Extra_Large'),
    ('L','Large'),
    ('M','Medium'),
    ('S','Small'),
    ('XS','XtraSmall')
]

type_customer =[
    ('M','mother'),
    ('B','baby')
]
mother_product=[
    ('PE','pregancy_essential'),
    ('Cl','clothing'),
    ('B','beauty'),
    ('J','jewllery'),
    ('WN','willness'),
    ('PC','Podcast')
]
gender =[
    ('M','male'),
    ('F','female')
]

baby_product=[
    ('NBE','new_born_essential'),
    ('TD','toddlers'),
    ('BS','bestseller'),
    ('FW','footwear'),
    ('KC','kidscare'),
    ('KF','kidsfedding')



]

class Product(models.Model):
    vendor_name = models.ForeignKey(ProfileVendor,on_delete=models.CASCADE)
    customer_type= models.CharField(max_length=20,choices=type_customer,default=None)
    product_nature_mother = models.CharField(max_length=20,choices=mother_product,default=None)
    product_nature_baby = models.CharField(max_length=20,choices=baby_product,default=None)
    baby_gender = models.CharField(max_length=10,choices=gender,default=None)
    Name = models.CharField(max_length=100,blank=True)
    product_color_blue = models.ImageField(upload_to='media',blank=True)
    product_color_orange = models.ImageField(upload_to='media',blank=True)
    product_color_green = models.ImageField(upload_to='media',blank=True)
    product_color_pink = models.ImageField(upload_to='media',blank=True)
    product_color_yellow = models.ImageField(upload_to='media',blank=True)
    product_size = models.CharField(max_length=20,choices=product_size,default='M')
    Price = models.PositiveIntegerField()
   
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.Name
    


class OrderCustomer(models.Model):
    
    
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    complete = models.BooleanField(default=False)
    Order_data= models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.user)
class OrderIteamCustomer(models.Model):
    vendor_name = models.ForeignKey(ProfileVendor,on_delete=models.CASCADE,null=True)
    
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(blank=True,null=True)
    selected_image = models.ImageField(upload_to='media',null=True)
    product_sizing = models.CharField(max_length=20,choices=product_size)
    order = models.ForeignKey(OrderCustomer,on_delete=models.CASCADE)
    carted = models.BooleanField(default=False)
    Carted_date= models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property    
    def total_price(self):
        price = self.product.Price
        total_price = self.quantity*price 
        return total_price
    @property
    def grand_total_price(self):
        grand_total = sum( value for value in self.total_price)
        return grand_total

    
        


class ShippingAddress(models.Model):
    city = models.CharField(max_length=100,default='kathmandu')
    province = models.CharField(max_length=100,default='Bagmati')
    

