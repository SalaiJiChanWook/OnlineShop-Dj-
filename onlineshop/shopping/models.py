from django.db import models

# Create your models here.
class Catigories(models.Model):
   name = models.CharField(max_length=255,null=True)
   slug_name = models.SlugField(max_length=255,null=True, unique=name)
   digital = models.BooleanField(default=False, null=True,blank=True)


class Manfashion(models.Model):
    name = models.CharField(max_length=255,null=True)
    catigory = models.ForeignKey(Catigories, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(max_length=255,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True,upload_to= 'Manfashion')
    
    def __str__(self):
         return self.name
     
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 
    
class ManfashionBestSeller(models.Model):
    name = models.CharField(max_length=255,null=True)
    catigory = models.ForeignKey(Catigories, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(max_length=255,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True,upload_to= 'ManfashionSubCategory')
    
    def __str__(self):
         return self.name
     
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 


class Womenfashion(models.Model):
    name = models.CharField(max_length=255,null=True)
    catigory = models.ForeignKey(Catigories, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(max_length=255,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True,upload_to= 'WomenfashionCategory')
    
    def __str__(self):
         return self.name
     
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 
        
class WomenfashionBestSeller(models.Model):
    name = models.CharField(max_length=255,null=True)
    catigory = models.ForeignKey(Catigories, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(max_length=255,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True,upload_to= 'WomenfashionSubCategory')
    
    def __str__(self):
         return self.name
     
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 
    
    
class Computer(models.Model):
    name = models.CharField(max_length=255,null=True)
    catigory = models.ForeignKey(Catigories, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(max_length=255,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True,upload_to= 'Computers')
    
    def __str__(self):
         return self.name
     
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 
    
    
class Laptop(models.Model):
    name = models.CharField(max_length=255,null=True)
    catigory = models.ForeignKey(Catigories, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(max_length=255,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True,upload_to= 'Laptops')
    
    def __str__(self):
         return self.name
     
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 


class Mobile(models.Model):
    name = models.CharField(max_length=255,null=True)
    catigory = models.ForeignKey(Catigories, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(max_length=255,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True,upload_to= 'Mobiles')
    
    def __str__(self):
         return self.name
     
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 


class Neklace(models.Model):
    name = models.CharField(max_length=255,null=True)
    catigory = models.ForeignKey(Catigories, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(max_length=255,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True,upload_to= 'Mobiles')
    
    def __str__(self):
         return self.name
     
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 


class Ring(models.Model):
    name = models.CharField(max_length=255,null=True)
    catigory = models.ForeignKey(Catigories, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(max_length=255,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True,upload_to= 'Mobiles')
    
    def __str__(self):
         return self.name
     
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 


class EarRing(models.Model):
    name = models.CharField(max_length=255,null=True)
    catigory = models.ForeignKey(Catigories, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(max_length=255,null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True,upload_to= 'Mobiles')
    
    def __str__(self):
         return self.name
     
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 
    
    
from userauths.models import User

class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
class ElectronicProduct(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	digital = models.BooleanField(default=False,null=True, blank=True)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url


class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
		
	@property
	def shipping(self):
		shipping = False
		orderitems = self.orderitem_set.all()
		for i in orderitems:
			if i.product.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Catigories, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total

class ShippingAddress(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address
