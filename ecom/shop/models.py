from django.db import models

# Create your models here.

class Product(models.Model):
    product_id =  models.AutoField
    product_name =models.CharField(max_length=50)
    product_category =models.CharField(max_length=50,default="")
    product_price =models.IntegerField(default=0)
    product_desc= models.CharField(max_length=300)
    pub_date= models.DateField()
    product_image=models.ImageField(upload_to="shop/images",default="")


    def __str__(self):
        return self.product_name

class Contact(models.Model):

    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_no = models.IntegerField(default=0)
    suggestion =models.CharField(max_length=500)



    def __str__(self):

     return self.name




class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip = models.IntegerField()
    phone = models.IntegerField()




class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."