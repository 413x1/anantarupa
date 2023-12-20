from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=20)
    join_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Items(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'items'


class Catalogs(models.Model):
    item = models.ForeignKey('Items', models.DO_NOTHING)
    price = models.IntegerField()
    currency = models.ForeignKey('Currencies', models.DO_NOTHING)
    max_user_stack = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catalogs'


class Currencies(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'currencies'


class UserCurrencies(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    currency = models.ForeignKey(Currencies, models.DO_NOTHING, blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_currencies'


class Transactions(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    catalog = models.ForeignKey(Catalogs, models.DO_NOTHING)
    qty = models.IntegerField()
    total_price = models.IntegerField()
    created_at = models.DateTimeField()
    status = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'transactions'


class UserItems(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING)
    item = models.ForeignKey(Items, models.DO_NOTHING)
    qty = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_items'



