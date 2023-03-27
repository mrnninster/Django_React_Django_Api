from rest_framework import serializers
from .models import AccountsModel

class CreateAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountsModel
        fields = ("server_name","login_id","platform","password")

class ViewAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountsModel
        fields = ("account_id","server_name","login_id","platform")