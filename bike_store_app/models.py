from django.db import models

class login(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    usertype=models.CharField(max_length=200)

class shop(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    post=models.CharField(max_length=200)
    pin=models.CharField(max_length=200)
    place=models.CharField(max_length=200)
    LOGIN=models.ForeignKey(login,default=1,on_delete=models.CASCADE)

class user(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    post = models.CharField(max_length=200)
    pin = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    LOGIN = models.ForeignKey(login, default=1, on_delete=models.CASCADE)

class complaints(models.Model):
    date=models.CharField(max_length=200)
    complaint=models.CharField(max_length=200)
    reply=models.CharField(max_length=200)
    reply_date=models.CharField(max_length=200)
    USER=models.ForeignKey(user, default=1, on_delete=models.CASCADE)

class rating(models.Model):
    date=models.CharField(max_length=200)
    rating=models.CharField(max_length=200)
    USER = models.ForeignKey(user, default=1, on_delete=models.CASCADE)

class parts_category(models.Model):
    category=models.CharField(max_length=200)

class service(models.Model):
    service_name=models.CharField(max_length=200)

class bike(models.Model):
    name=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    model=models.CharField(max_length=200)
    SHOP=models.ForeignKey(shop,default=1,on_delete=models.CASCADE)

class parts(models.Model):
    name=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    manufacture_company=models.CharField(max_length=200)
    SHOP = models.ForeignKey(shop, default=1, on_delete=models.CASCADE)
    PARTS_CATEGORY=models.ForeignKey(parts_category,default=1,on_delete=models.CASCADE)

class order(models.Model):
    price=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    payment_status=models.CharField(max_length=200)
    payment_date=models.CharField(max_length=200)
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)
    SHOP=models.ForeignKey(shop,default=1,on_delete=models.CASCADE)

class order_sub(models.Model):
    quantity=models.CharField(max_length=200)
    ORDER=models.ForeignKey(order,default=1,on_delete=models.CASCADE)
    PARTS=models.ForeignKey(parts,default=1,on_delete=models.CASCADE)

class cart(models.Model):
    quantity=models.CharField(max_length=200)
    PARTS=models.ForeignKey(parts,default=1,on_delete=models.CASCADE)
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)

class ownservice(models.Model):
    amount=models.CharField(max_length=200)
    SERVICE=models.ForeignKey(service,default=1,on_delete=models.CASCADE)
    SHOP=models.ForeignKey(shop,default=1,on_delete=models.CASCADE)

class service_request(models.Model):
    status=models.CharField(max_length=200)
    date=models.CharField(max_length=200)
    OWNSERVICE=models.ForeignKey(ownservice,default=1,on_delete=models.CASCADE)
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)

class bike_request(models.Model):
    date=models.CharField(max_length=200)
    status=models.CharField(max_length=200)
    BIKE=models.ForeignKey(bike,default=1,on_delete=models.CASCADE)
    USER=models.ForeignKey(user,default=1,on_delete=models.CASCADE)


