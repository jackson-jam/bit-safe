# models.py
from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=32)
    user_password = models.CharField(max_length=32)
    user_email = models.CharField(max_length=64,default='1')


class Vendors(models.Model):
    # vender_id = models.CharField(max_length=20)
    vender_name = models.CharField(max_length=255)
    vender_address = models.CharField(max_length=255)
    vender_city = models.CharField(max_length=255)
    vender_zip = models.CharField(max_length=255)  # 邮编
    vender_country = models.CharField(max_length=255)


class Products(models.Model):
    # prod_id = models.CharField(max_length=10)
    prod_name = models.CharField(max_length=255)  # 产品名
    prod_price = models.CharField(max_length=255)  # 产品价格
    prod_desc = models.CharField(max_length=255)  # 产品描述


class Customers(models.Model):
    # cust_id = models.CharField(max_length=20)
    cust_name = models.CharField(max_length=255)
    cust_address = models.CharField(max_length=255)
    cust_city = models.CharField(max_length=255)
    cust_zip = models.CharField(max_length=255)  # 邮编
    cust_country = models.CharField(max_length=255)
    cust_contact = models.CharField(max_length=20)
    cust_email = models.CharField(max_length=255)
    cust_num = models.CharField(max_length=255)


class Trend(models.Model):
    user_id = models.CharField(max_length=20)
    integral = models.CharField(max_length=255)
    sea_num = models.CharField(max_length=255)
    coll_num = models.CharField(max_length=255)
    pur_num = models.CharField(max_length=255)
    buy_num = models.CharField(max_length=255)
    cunsume = models.CharField(max_length=20)


class Shopping(models.Model):
    user_id = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    item_int = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    item_price = models.CharField(max_length=255)
    add_time = models.CharField(max_length=255)
    item_num = models.CharField(max_length=255)


class Order(models.Model):
    order_num = models.CharField(max_length=20)
    order_data = models.CharField(max_length=255)


class Classify(models.Model):
    class_name = models.CharField(max_length=20)
    create_time = models.CharField(max_length=255)
    update_time = models.CharField(max_length=255)
    rank = models.CharField(max_length=255)


class Appraise(models.Model):
    order_num = models.CharField(max_length=20)
    username = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    like = models.CharField(max_length=255)
    appraise = models.CharField(max_length=255)


class Browse(models.Model):
    item_name = models.CharField(max_length=20)
    username = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
