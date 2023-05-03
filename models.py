from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class user(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    email = models.EmailField(db_column="email", unique=True)
    phone = models.BigIntegerField(db_column="phone", unique=True)
    adress = models.CharField(db_column="adress")

    def __str__(self):
        return self.email

    class Meta:
        db_table = "user"
        verbose_name = "Пользователь"


class delievery(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    price = models.DecimalField(
        db_column="price", max_digits=8, decimal_places=2
    )
    type_name = models.CharField(db_column="type_name")

    def __str__(self):
        return self.type_name

    class Meta:
        db_table = "delievery"
        verbose_name = "Доставка"


class category(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    name = models.CharField(db_column="name")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "category"
        verbose_name = "Категория"


class product(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    category_id = models.ForeignKey(
        category,
        to_field="id",
        db_column="category_id",
        on_delete=models.CASCADE,
    )
    amt = models.IntegerField(db_column="amt")
    name = models.CharField(db_column="name")
    description = models.CharField(
        db_column="description", max_length=1000
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"
        verbose_name = "Товар"


class order_items(models.Model):
    id = models.AutoField(primary_key=True, db_column="id")
    order_id = models.IntegerField(db_column="order_id")
    product_id = models.ForeignKey(
        product,
        to_field="id",
        on_delete=models.CASCADE,
        db_column="product_id",
    )
    quantity = models.IntegerField(db_column="quantity")
    price = models.DecimalField(
        max_digits=8, decimal_places=2, db_column="price"
    )

    def __float__(self):
        return self.price

    class Meta:
        db_table = "order_items"
        verbose_name = "Корзина"


class order(models.Model):
    id = models.AutoField(db_column="id", primary_key=True)
    order_items_id = models.ForeignKey(
        order_items,
        to_field="id",
        on_delete=models.CASCADE,
        db_column="order_items_id",
    )
    user_id = models.ForeignKey(
        User,
        to_field="id",
        on_delete=models.CASCADE,
        db_column="user_id",
    )
    delievery_id = models.ForeignKey(
        delievery,
        to_field="id",
        on_delete=models.CASCADE,
        db_column="delievery_id",
    )
    date = models.DateField(auto_now_add=True, db_column="date")

    class Meta:
        db_table = "order"
        verbose_name = "Заказ"
