from django.db import models

# Create your models here.
#caregory models
class Category(models.Model):
    name = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return self.name
   
# client models
class Record(models.Model):
    category =  models.ForeignKey(Category,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.IntegerField()
    tall = models.IntegerField()
    wedight = models.IntegerField()
    address = models.CharField(max_length=250)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return self.first_name + " " + self.last_name
   
    class Meta:
       ordering = ['-create_at']