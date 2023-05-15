from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from autoslug import AutoSlugField
# Create your models here.
STATE_CHOICES =(
('Andman & Nicobar Islands', 'Andaman & Nicobar Islands'),
('Andhra Pardesh ', 'Andhra Pardesh'),
('Arunachal Pardesh ', 'Arunachal Pardesh'),
('Asam ', 'Asam'),
('Bihar ', 'Bihar'),
('Chandigarh ', 'Chandigarh'),
('Chhatisgarh ', 'Chhatisgarh '),
('Delhi','Delhi'),
('Gujarat0','Gujarat'),
('Himachal Pardesh','Himachal Pardesh'),
('Haryana', 'Haryana'),
('Jammu & Kashmir','Jammu & Kashmir'),
('Jharkhand','Jharkhand'),
('Karnataka','Karnataka'),
('Kerala','Kerala'),
('Lakshadweep','Lakshadweep'),
('Madhya Pardesh','Madhya Pardesh'),
('Maharashtra','Maharashtra'),
('Manipur','Manipur'),
('Meghalaya','Meghalaya'),
('Mizoram','Mizoram'),
('Nagaland','Nagaland'),
('Odisha','Odisha'),
('Puducherry','Puducherry'),
('Punjab','Punjab'),
('Rajashtan','Rajasthan'),
('Skkim','Sikkim'),
('Tamil Nadu','Tamil Nadu'),
('Telangana','Telangana'),
('Uttarakhand','Uttarkhand'),
('Utar Pardesh','Utar Pardesh'),
('West Bengal','West Bengal'),

)
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)

CATEGORY_CHOICES = (
        ('M', 'MOBILE'),
        ('L' ,'LAPTOP'),
        ('TW', 'Top Wear'),
        ('BW','Bottom Wear'),
        ('AC','ACCESSORIES'),
        ('FO', 'FOOTWEAR'),
        ('WO','WATCHES'),
        ('SH','SHIRTS')
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    product_slug = AutoSlugField(populate_from='title',unique=True, null=True, default=None)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='productimg')


    def delete(self,*args, **kwargs):
        self.product_image.delete()
        return super(Product, self).delete(*args, **kwargs)
    
    def __str__(self) :
        return str(self.title)

    def admin_photo(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.product_image.url))
    admin_photo.short_description ='product_image'
    admin_photo.allow_tag =True
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self) :
        return str(self.id)
    @property
    def total_cost(self):
     return self.quantity * self.product.discounted_price
    
STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status =models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')

    
    @property
    def total_cost(self):
     return self.quantity * self.product.discounted_price

   
