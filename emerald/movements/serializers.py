from rest_framework import serializers
from django.contrib.auth.models import User
from . import models as pm


class UserSerializer(serializers.ModelSerializer):
    account_types = serializers.PrimaryKeyRelatedField(many=True, queryset=pm.AccountType.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'account_types')


class AccountTypeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = pm.AccountType
        fields = ('id', 'name', 'owner')


class CardTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = pm.CardType
        fields = ('id', 'name')


class TransactionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = pm.TransactionType
        fields = ('id', 'name')


class ProjectTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = pm.ProjectType
        fields = ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = pm.Category
        fields = ('id', 'name', 'logo')


class SubcategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = pm.Subcategory
        fields = ('id', 'name', 'category', 'logo')


class EntitySerializer(serializers.ModelSerializer):

    class Meta:
        model = pm.Entity
        fields = ('id', 'name', 'logo')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = pm.Customer
        fields = ('id', 'first_name', 'last_name', 'phone', 'photo')


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = pm.Account
        fields = ('id', 'iban', 'alias', 'balance', 'currency', 'account_type', 'entity', 'customers')


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = pm.Project
        fields = ('id', 'name', 'description', 'project_type')


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = pm.Card
        fields = ('id', 'alias', 'number', 'expiration_date', 'card_type', 'customer', 'account')


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = pm.Transaction
        fields = ('id', 'concept', 'operation_date', 'value_date', 'amount', 'comment', 'transaction_type',
                  'card', 'account', 'subcategory', 'project', 'referenced_transaction', 'currency')
