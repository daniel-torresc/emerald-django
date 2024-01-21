from rest_framework import serializers
from django.contrib.auth.models import User
from . import models as pm


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'last_login')


class AccountTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = pm.AccountType
        exclude = ('id', )


class CardTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = pm.CardType
        exclude = ('id', )


class TransactionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = pm.TransactionType
        exclude = ('id', )


class ProjectTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = pm.ProjectType
        exclude = ('id', 'owner')


class CategorySerializer(serializers.ModelSerializer):
    subcategories = serializers.StringRelatedField(many=True)

    class Meta:
        model = pm.Category
        exclude = ('id', 'owner')


class SubcategorySerializer(serializers.ModelSerializer):
    # category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = pm.Subcategory
        exclude = ('id', 'owner')


class EntitySerializer(serializers.ModelSerializer):

    class Meta:
        model = pm.Entity
        exclude = ('id', )


class CustomerSerializer(serializers.HyperlinkedModelSerializer):  # TODO: check if HyperlinkedModelSerializer is better

    class Meta:
        model = pm.Customer
        exclude = ('owner', )
        # exclude = ('id', 'owner')


class AccountSerializer(serializers.ModelSerializer):
    # account_type = serializers.StringRelatedField(read_only=True)
    # entity = serializers.StringRelatedField(read_only=True)
    # customers = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:
        model = pm.Account
        exclude = ('id', 'owner')


class ProjectSerializer(serializers.ModelSerializer):
    # project_type = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = pm.Project
        exclude = ('id', 'owner')


class CardSerializer(serializers.ModelSerializer):
    # card_type = serializers.StringRelatedField(read_only=True)
    # customer = serializers.StringRelatedField(read_only=True)
    # account = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = pm.Card
        exclude = ('id', 'owner')


class TransactionSerializer(serializers.ModelSerializer):
    transaction_type = serializers.StringRelatedField(read_only=True)
    # card = serializers.StringRelatedField(read_only=True)
    # account = serializers.StringRelatedField(read_only=True)
    # subcategory = serializers.StringRelatedField(read_only=True)
    # project = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = pm.Transaction
        exclude = ('owner', )
