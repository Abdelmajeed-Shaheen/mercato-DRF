from django.db import models

class Category (models.Model):
	name = models.CharField(max_length = 100)
	image = models.ImageField(null=True , blank = True)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.name

class Subcategory (models.Model):
	name = models.CharField(max_length = 100)
	image = models.ImageField(null=True , blank = True)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)

	class Meta:
		verbose_name_plural = "Sub-Categories"
	def __str__(self):
		return self.name

class Item (models.Model):
	name = models.CharField(max_length = 100)
	image = models.ImageField(null=True , blank = True)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	descreption = models.TextField()
	in_stock = models.IntegerField()
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	sub_category = models.ForeignKey(Subcategory, on_delete = models.CASCADE)

	def __str__(self):
		return self.name
