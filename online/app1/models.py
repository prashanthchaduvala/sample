from django.db import models

class Savemodel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    contact = models.IntegerField()
    email = models.EmailField(max_length=40,unique=True)
    password = models.CharField(max_length=50)


class Merchantmodel(models.Model):
    p_no=models.IntegerField(primary_key=True)
    p_name=models.CharField(max_length=30)
    p_price=models.FloatField()
    p_qty=models.IntegerField()
    merchant=models.ForeignKey(Savemodel,on_delete=models.CASCADE,default=False)

