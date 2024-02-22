from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=20)


    def __str__(self):
        return self.name
    def pub(self):
        return self.name

class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    dec=models.CharField(blank=True,default="",max_length=100,)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    # image=models.ImageField(upload_to='static/image/')
    off=models.BooleanField(default=False,null=True)
    offprice=models.IntegerField(null=True)

    def __str__(self):
        return self.name+"\t"+str(self.price)+"\t"+str(self.dec)+str(self.off)+"/t"+str(self.offprice)
    def pub(self):
        return self.name+"\t"+str(self.price)+"\t"+str(self.dec)+str(self.off)+"/t"+str(self.offprice)


# Create your models here.
