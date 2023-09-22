from django.db import models
from django.contrib.auth.models import User


STATE_CHOICES=(
('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'),
('Andhra Pradesh', 'Andhra Pradesh'),
('Arunachal Pradesh', 'Arunachal Pradesh'),
('Assam', 'Assam'),
('Bihar', 'Bihar'),
('Chandigarh', 'Chandigarh'),
('Chhattisgarh', 'Chhattisgarh'),
('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'),
('Delhi', 'Delhi'),
('Goa', 'Goa'),
('Gujarat', 'Gujarat'),
('Haryana', 'Haryana'),
('Himachal Pradesh', 'Himachal Pradesh'),
('Jammu and Kashmir', 'Jammu and Kashmir'),
('Jharkhand', 'Jharkhand'),
('Karnataka', 'Karnataka'),
('Kerala', 'Kerala'),
('Ladakh', 'Ladakh'),
('Lakshadweep', 'Lakshadweep'),
('Madhya Pradesh', 'Madhya Pradesh'),
('Maharashtra', 'Maharashtra'),
('Manipur', 'Manipur'),
('Meghalaya', 'Meghalaya'),
('Mizoram', 'Mizoram'),
('Nagaland', 'Nagaland'),
('Odisha', 'Odisha'),
('Puducherry', 'Puducherry'),
('Punjab', 'Punjab'),
('Rajasthan', 'Rajasthan'),
('Sikkim', 'Sikkim'),
('Tamil Nadu', 'Tamil Nadu'),
('Telangana', 'Telangana'),
('Tripura', 'Tripura'),
('Uttar Pradesh', 'Uttar Pradesh'),
('Uttarakhand', 'Uttarakhand'),
('West Bengal', 'West Bengal')

)

# Create your models here.
CATEGORY_CHOICES=(
    ('JN','Jeans'),
    ('SH','Shirts'),
    ('BL','Blazers'),
    ('SO','Shoes'),
    ('HT','Hats'),
    ('SJ','Sports Jersey'),
    ('HO','Hoodies'),
)

STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the Way','On the Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
)

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discount_price=models.FloatField()
    description=models.TextField()
    prodapp=models.TextField(default='')
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='product')
    def __str__(self):
        return self.title

class Customer(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    Name=models.CharField(max_length=200)
    Locality=models.CharField(max_length=200)
    City=models.CharField(max_length=50)
    Mobile=models.IntegerField(default=0)
    Zipcode=models.IntegerField()
    State=models.CharField(choices=STATE_CHOICES,max_length=100)
    def __str__(self):
        return self.Name
    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)


class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    amount=models.FloatField()
    razorpay_order_id=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status=models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id=models.CharField(max_length=225,blank=True,null=True)
    paid=models.BooleanField(default=False)
    


class OrderPlaced(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
    payment=models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price
    
class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

