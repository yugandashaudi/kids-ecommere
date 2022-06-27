from sqlite3 import apilevel
from xml.sax import parseString
from django.shortcuts import render
from numpy import true_divide

from .custom_permission_for_vendors import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework.permissions import IsAuthenticated


class CreateProductView(APIView):
    permission_classes=[VendorPermission]

    def get(self,request,format=None):
        Product_data = Product.objects.all()
        serializer = CreateProductSerializer(Product_data,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer = CreateProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response('The product iteam was added')




class UpdateAndDeleteView(APIView):
    permission_classes = [VendorPermission]
    def delete(self,request,id,format=None):
        selected_product = Product.objects.filter(id=id).first()
        selected_product.delete()
        return Response('The selected product is deleted ')

    def put(self,request,id,format=None):
        permission_classes =[VendorPermission]
        selected_product = Product.objects.filter(id=id).first() 
        serializer = CreateProductSerializer(selected_product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('The product has been updated')




           
class GetOrderView(APIView):
    permission_class = [VendorPermission]
    def get(self,request,format=None):
        vendor_naming = ProfileVendor.objects.get(user=request.user)
        completed_ordered_product = OrderCustomer.objects.filter(complete=True,vendor_name=vendor_naming)
        for something in completed_ordered_product:
            ordered_product = something.orderiteamcustomer_set.all()
    
        
        serializer = OrderIteamCustomerSerializer(ordered_product,many=True)
        return Response(serializer.data)







class CreateOrderByCustomer(APIView):
    'This is the view to get all the products and the cart total '
    permisssion_classes =[IsAuthenticated]
    def get(self,request,format=None):
        all_products = Product.objects.all()
        user_order = OrderCustomer.objects.create(user=request.user)
        quantity = OrderIteamCustomer.objects.filter(carted=True,order=user_order)
        for quan in quantity:
            total += quan.quantity

        serializer = CreateProductSerializer(all_products,many=True)

        return Response({'data':serializer.data,'cart_total':total})
    def post(self,request,format=None):
        Create_order,created = OrderCustomer.objects.get_or_create(user=request.user)
        id=Create_order
        serializer = ProductIdActtionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        action =serializer.data.get('action')
        id = serializer.data.get('product')
        print(id)
        print(action)
        
        
       
       
        if action == 'Add':
            product = Product.objects.filter(id=id).first()
            print(product)
            
            list=[product.product_color_blue,product.product_color_yellow,
            product.product_color_pink,product.product_color_orange]

            image_list=next(image for image in list if image is not None)
            print(image_list)
                            
                            


            OrderIteam,created = OrderIteamCustomer.objects.get_or_create(vendor_name=product.vendor_name,
            product=product,order=Create_order,selected_image=image_list,product_sizing=product.product_size,carted=True)

            if created:
                print('created')
                quantity=0
                quantity+=1
                OrderIteam.quantity=quantity
                OrderIteam.save()

            else:
                print('geted')
                
                OrderIteam.quantity =(OrderIteam.quantity)+1  
                OrderIteam.save()




                   
                    

       

           
                

        if action == 'remove':
            product = Product.objects.filter(id=id).first()
            list=[product.product_color_blue,product.product_color_yellow,
            product.product_color_pink,product.product_color_orange]

            image_list=next(image for image in list if image is not None)

            OrderIteam = OrderIteamCustomer.objects.filter(vendor_name=product.vendor_name,
            product=product,order=Create_order,selected_image=image_list,product_sizing=product.product_size,carted=True).first()

            OrderIteam.quantity=(OrderIteam.quantity)-1
            OrderIteam.save()  

            if OrderIteam.quantity == 0:
                OrderIteam.delete()

           
        return Response({'msg':'the action','action':action,'msg':'performed sucessfullyy','qauntity':OrderIteam.quantity})        



    



            





        
       
      
        


class CheckOutPage(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        user_order = OrderCustomer.objects.get(user=request.user)
        quantity = OrderIteamCustomer.objects.filter(carted=True,order=user_order)

        total_price = 0
        grand_total_price = 0
        total=0
       
        for quan in quantity:
            total += quan.quantity
            print(total)
            total_price = quan.total_price
           
            
    

        serializer = OrderIteamCustomerSerializer(quantity,many=True)    

        return Response({'data':serializer.data,'total':total,'total_price':total_price})

    
      
    def post(self,request,format=None):
        user_order = OrderCustomer.objects.filter(user=request).first()
        orderiteamlist = OrderIteamCustomer.objects.filter(carted=True,order=user_order)
        serializer = CheckOutProductAddSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        button = serializer.validated_data.get('button')
        id = serializer.validated_data.get('id')
        selected_order_iteam = OrderIteamCustomer.objects.filter(id=id,order=request.user).first()
        if button == "Add":
            selected_order_iteam.quantity = (selected_order_iteam.quantity)+1
            selected_order_iteam.save()

        elif button =="Remove":
            selected_order_iteam.quantity = (selected_order_iteam.quantity)-1
            selected_order_iteam.save()
            if selected_order_iteam.quantity == 0:
                selected_order_iteam.delete()

        return Response({'msg':'the action','action':button,'last_msg':
        'was done sucessfully','quantity':selected_order_iteam.qauntity,})        


       
     