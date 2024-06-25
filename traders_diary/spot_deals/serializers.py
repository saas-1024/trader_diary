import io

from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import SpotDeal


class SpotDealSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpotDeal
        fields = ('asset_name', 'asset_price', 'asset_amount', 'usd_amount', 'comission', 'trade_side', 'comment',
                  "exchange", 'user_deal')

    def create(self, validated_data):
        return SpotDeal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.asset_name = validated_data.get("asset_name")
        instance.asset_price = validated_data.get("asset_price")
        instance.asset_amount = validated_data.get("asset_amount")
        instance.usd_amount = validated_data.get("usd_amount")
        instance.comission = validated_data.get("comission")
        instance.trade_side = validated_data.get("trade_side")
        instance.comment = validated_data.get("comment")
        instance.exchange = validated_data.get("exchange")
        instance.save()
        return instance

    def delete(self, instance, validated_data):
        instance.asset_name = validated_data.get("asset_name")
        instance.asset_price = validated_data.get("asset_price")
        instance.asset_amount = validated_data.get("asset_amount")
        instance.usd_amount = validated_data.get("usd_amount")
        instance.comission = validated_data.get("comission")
        instance.trade_side = validated_data.get("trade_side")
        instance.comment = validated_data.get("comment")
        instance.exchange = validated_data.get("exchange")
        instance.delete()
        return str("Deal deleted")
