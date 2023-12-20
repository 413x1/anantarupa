from rest_framework import serializers
from .models import Users, Catalogs, Transactions, UserCurrencies, UserItems
from django.db import transaction
from datetime import datetime


class PurchaseSerializer(serializers.ModelSerializer):
    item_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField()

    user = None
    catalog = None
    user_currency = None
    user_item = None

    class Meta:
        model = Transactions
        fields = '__all__'
        read_only_fields = [
            'user',
            'catalog',
            'qty',
            'total_price',
            'created_at',
            'status'
        ]

    def validate(self, attrs):
        super().validate(attrs)
        
        user_id = attrs["user_id"]
        item_id = attrs["item_id"]

        # validate user existence
        if not Users.objects.filter(pk=user_id).exists():
            raise serializers.ValidationError({'user_id': 'Invalid user_id'})
        
        # validate things that is not listed in the shop,
        if not Catalogs.objects.filter(item_id=item_id).exists():
            raise serializers.ValidationError({'item_id': 'Invalid item_id'})
        
        self.user = Users.objects.get(pk=user_id)
        self.catalog = Catalogs.objects.filter(item_id=item_id).first()
        self.user_item = UserItems.objects.filter(user_id=user_id, item_id=item_id)
        self.user_currency = UserCurrencies.objects.filter(user_id=user_id, currency=self.catalog.currency)

        user_stock = self.user_item.first().qty if self.user_item else 0 or 0
        user_balance = self.user_currency.first().amount if self.user_currency else 0 or 0

        if user_stock >= self.catalog.max_user_stack:
            raise serializers.ValidationError({'item_id': 'Invalid item exceeds maximum stack'})
        if user_balance < self.catalog.price:
            raise serializers.ValidationError({'user_id': 'Invalid user balance not enough'})

        return attrs
    
    @transaction.atomic
    def create(self, _):
        try:
            trx = Transactions.objects.create(
                user=self.user,
                catalog=self.catalog,
                qty=1,
                total_price=self.catalog.price,
                created_at=datetime.now(),
            )

            user_currency = self.user_currency.first()
            user_currency.amount = user_currency.amount - trx.total_price
            user_currency.save()
            
            if not self.user_item:
                UserItems.objects.create(
                    user=self.user,
                    item=self.catalog.item,
                    qty=1
                )
            else:
                user_item = self.user_item.first()
                user_item.qty = user_item.qty + 1
                user_item.save()
            
            trx.status = 'success'

            return trx
    
        except Exception as e:
            print(str(e))
            raise serializers.ValidationError(
                {"server": "Error create transaction"}
            )



        

