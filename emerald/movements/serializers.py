from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class UserSerializer(serializers.ModelSerializer):
    account_types = serializers.PrimaryKeyRelatedField(many=True, queryset=models.AccountType.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'account_types')


class AccountTypeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = models.AccountType
        fields = ('id', 'account_type_name', 'owner')


class CardTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CardType
        fields = ('id', 'card_type_name')


class TransactionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TransactionType
        fields = ('id', 'transaction_type_name')


class ProjectTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProjectType
        fields = ('id', 'project_type_name')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = ('id', 'category_name', 'category_logo')


class SubcategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Subcategory
        fields = ('id', 'subcategory_name', 'category', 'subcategory_logo')


class EntitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Entity
        fields = ('id', 'entity_name', 'entity_logo')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Customer
        fields = ('id', 'first_name', 'last_name', 'phone', 'photo')


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Account
        fields = ('id', 'iban', 'account_alias', 'balance', 'currency', 'account_type', 'entity', 'customers')


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = ('id', 'project_name', 'project_description', 'project_type')


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Card
        fields = ('id', 'card_alias', 'card_number', 'expiration_date', 'card_type', 'customer', 'account')


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Transaction
        fields = ('id', 'concept', 'operation_date', 'value_date', 'amount', 'transaction_comment', 'transaction_type',
                  'card', 'account', 'subcategory', 'project', 'referenced_transaction', 'currency')
