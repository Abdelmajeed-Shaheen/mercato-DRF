from django.db import models
from django.contrib.auth.models import User

class Category (models.Model):
	name = models.CharField(max_length = 100)
	image = models.URLField(max_length=400,null=True,blank=True)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.name

class Subcategory (models.Model):
	name = models.CharField(max_length = 100)
	image = models.URLField(max_length=400,null=True,blank=True)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)

	class Meta:
		verbose_name_plural = "Sub-Categories"
	def __str__(self):
		return self.name

class Item (models.Model):
	name = models.CharField(max_length = 100)
	image = models.URLField(max_length=400,null=True,blank=True)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	descreption = models.TextField()
	in_stock = models.IntegerField()
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	sub_category = models.ForeignKey(Subcategory, on_delete = models.CASCADE)

	def __str__(self):
		return self.name

class OrderItem(models.Model):
	order=models.ForeignKey("Order",on_delete=models.CASCADE)
	item=models.ForeignKey(Item,on_delete=models.CASCADE)
	quantity=models.PositiveIntegerField(default=1)

class Order(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	products =models.ManyToManyField(Item,through=OrderItem)
	def __str__(self):
		return f'{self.user.username} Order {self.id}'
