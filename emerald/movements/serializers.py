from rest_framework import serializers
from django.contrib.auth.models import User
from . import models as pm


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"  # ('id', 'username', 'account_types')


class AccountTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = pm.AccountType
        fields = "__all__"  # ('id', 'name')


class CardTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = pm.CardType
        fields = "__all__"  # ('id', 'name')


class TransactionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = pm.TransactionType
        fields = "__all__"  # ('id', 'name')


class ProjectTypeSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = pm.ProjectType
        fields = "__all__"  # ('id', 'name')


class CategorySerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = pm.Category
        fields = "__all__"  # ('id', 'name', 'logo')


class SubcategorySerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = pm.Subcategory
        fields = "__all__"  # ('id', 'name', 'category', 'logo')


class EntitySerializer(serializers.ModelSerializer):

    class Meta:
        model = pm.Entity
        fields = "__all__"  # ('id', 'name', 'logo')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = pm.Customer
        fields = "__all__"  # ('id', 'first_name', 'last_name', 'phone', 'photo')


class AccountSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    account = AccountTypeSerializer(read_only=True)
    entity = EntitySerializer(read_only=True)
    customer = CustomerSerializer(read_only=True, many=True)

    class Meta:
        model = pm.Account
        fields = "__all__"  # ('id', 'iban', 'alias', 'balance', 'currency', 'account_type', 'entity', 'customers')


class ProjectSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    project_type = ProjectTypeSerializer(read_only=True)

    class Meta:
        model = pm.Project
        fields = "__all__"  # ('id', 'name', 'description', 'project_type')


class CardSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    card_type = CardTypeSerializer(read_only=True)
    customer = CustomerSerializer(read_only=True)
    account = AccountSerializer(read_only=True)

    class Meta:
        model = pm.Card
        fields = "__all__"  # ('id', 'alias', 'number', 'expiration_date', 'card_type', 'customer', 'account')


class TransactionSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    transaction_type = TransactionTypeSerializer(read_only=True)
    card = CardSerializer(read_only=True)
    account = AccountSerializer(read_only=True)
    subcategory = SubcategorySerializer(read_only=True)
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = pm.Transaction
        fields = "__all__"  # ('id', 'concept', 'operation_date', 'value_date', 'amount', 'comment', 'transaction_type', 'card', 'account', 'subcategory', 'project', 'referenced_transaction', 'currency')
